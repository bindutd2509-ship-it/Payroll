from datetime import date
from decimal import Decimal

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RunPayrollRequestSerializer
from .models import (
    SalaryStructure,
    SalaryStructureVersion,
    SalaryStructureComponentMapping,
    SalaryComponent,
    PayrollFormula,
)
from .payroll_engine import month_start_end, SafeExprEvaluator, PayrollLine


class RunPayrollAPIView(APIView):
    """
    POST /api/payrolls/run/
    Body: { company_id, month, year }
    """
    def post(self, request):
        ser = RunPayrollRequestSerializer(data=request.data)
        ser.is_valid(raise_exception=True)
        company_id = ser.validated_data["company_id"]
        month = ser.validated_data["month"]
        year = ser.validated_data["year"]

        start, end = month_start_end(year, month)

        # 1) Find an active salary structure for this company (pick latest created)
        structure = (
            SalaryStructure.objects
            .filter(company_id=company_id, is_active=True)
            .order_by("-created_at")
            .first()
        )
        if not structure:
            return Response(
                {"detail": "No active salary structure found for this company."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # 2) Find active version effective for this month
        # effective_from <= start and (effective_to is null OR effective_to >= start)
        version = (
            SalaryStructureVersion.objects
            .filter(
                salary_structure=structure,
                effective_from__lte=start,
            )
            .filter(
                # effective_to is null OR effective_to >= start
            )
        )
        # Django doesn't have OR filter shortcut without Q
        from django.db.models import Q
        version = version.filter(Q(effective_to__isnull=True) | Q(effective_to__gte=start)).order_by("-effective_from").first()

        if not version:
            return Response(
                {"detail": "No salary structure version effective for this month."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        mappings = (
            SalaryStructureComponentMapping.objects
            .select_related("salary_component", "formula")
            .filter(salary_structure_version=version)
            .order_by("display_order", "created_at")
        )

        if not mappings.exists():
            return Response(
                {"detail": "No component mappings found for this structure version."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Variables available to formulas
        variables = {}  # like {"BASIC": Decimal("25000")}
        evaluator = SafeExprEvaluator()

        lines = []
        gross = Decimal("0")
        deductions = Decimal("0")

        # helper to detect BASIC (you can customize logic)
        def normalize_var_name(name: str) -> str:
            return name.upper().replace(" ", "_")

        # First pass: compute FIXED items and set variables
        # (so formulas can refer to them)
        for m in mappings:
            comp = m.salary_component
            var = normalize_var_name(comp.name)

            amount = Decimal("0")
            if m.calculation_type == "FIXED":
                amount = Decimal(m.value or 0)
            elif m.calculation_type == "PERCENT":
                # percent of BASIC (must exist)
                if "BASIC" not in variables:
                    # try also BASIC_PAY etc
                    # If no BASIC computed yet, defer to second pass
                    continue
            elif m.calculation_type == "FORMULA":
                # defer formula to second pass
                continue

            variables[var] = amount

            lines.append(PayrollLine(
                component_id=str(comp.id),
                component_name=comp.name,
                component_type=comp.component_type,
                calculation_type=m.calculation_type,
                amount=amount,
                display_order=m.display_order,
            ))

        # Ensure BASIC variable mapping:
        # If your basic component name is "Basic Pay Feb2026" it becomes BASIC_PAY_FEB2026.
        # Recommended: name your base as exactly "BASIC" or "Basic".
        # As a fallback, map any var containing "BASIC" to BASIC if BASIC not present.
        if "BASIC" not in variables:
            for k, v in list(variables.items()):
                if "BASIC" in k:
                    variables["BASIC"] = v
                    break

        # Second pass: compute PERCENT and FORMULA items
        for m in mappings:
            comp = m.salary_component
            var = normalize_var_name(comp.name)

            # Skip if already computed
            if var in variables:
                continue

            amount = Decimal("0")

            if m.calculation_type == "PERCENT":
                if "BASIC" not in variables:
                    return Response(
                        {"detail": "PERCENT mapping needs a BASIC component amount available first."},
                        status=status.HTTP_400_BAD_REQUEST,
                    )
                pct = Decimal(m.value or 0)
                amount = (variables["BASIC"] * pct) / Decimal("100")

            elif m.calculation_type == "FORMULA":
                if not m.formula:
                    return Response(
                        {"detail": f"Mapping for {comp.name} is FORMULA but formula is null."},
                        status=status.HTTP_400_BAD_REQUEST,
                    )
                expr = m.formula.formula_expression
                try:
                    amount = evaluator.eval(expr, variables)
                except Exception as e:
                    return Response(
                        {"detail": f"Formula error for {comp.name}: {str(e)}", "expression": expr, "variables": {k: str(v) for k, v in variables.items()}},
                        status=status.HTTP_400_BAD_REQUEST,
                    )
            else:
                # FIXED but not previously computed
                amount = Decimal(m.value or 0)

            variables[var] = amount

            lines.append(PayrollLine(
                component_id=str(comp.id),
                component_name=comp.name,
                component_type=comp.component_type,
                calculation_type=m.calculation_type,
                amount=amount,
                display_order=m.display_order,
            ))

        # Totals
        lines_sorted = sorted(lines, key=lambda x: x.display_order)
        for ln in lines_sorted:
            # common assumption: component_type = EARNING or DEDUCTION
            if str(ln.component_type).upper() == "DEDUCTION":
                deductions += ln.amount
            else:
                gross += ln.amount

        net = gross - deductions

        return Response(
            {
                "company_id": str(company_id),
                "month": month,
                "year": year,
                "salary_structure_id": str(structure.id),
                "salary_structure_version_id": str(version.id),
                "lines": [
                    {
                        "component_id": l.component_id,
                        "component_name": l.component_name,
                        "component_type": l.component_type,
                        "calculation_type": l.calculation_type,
                        "amount": str(l.amount),
                        "display_order": l.display_order,
                    }
                    for l in lines_sorted
                ],
                "totals": {
                    "gross": str(gross),
                    "deductions": str(deductions),
                    "net": str(net),
                },
            },
            status=status.HTTP_201_CREATED,
        )