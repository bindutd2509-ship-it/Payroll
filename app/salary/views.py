from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from .models import (
    SalaryStructure,
    SalaryStructureVersion,
    SalaryComponent,
    PayrollFormula,
    SalaryStructureComponentMapping,
)

from .serializers import (
    SalaryStructureSerializer,
    SalaryStructureVersionSerializer,
    SalaryComponentSerializer,
    PayrollFormulaSerializer,
    SalaryStructureComponentMappingSerializer,
)


class SalaryStructureViewSet(viewsets.ModelViewSet):
    queryset = SalaryStructure.objects.all().order_by("-created_at")
    serializer_class = SalaryStructureSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["company_id", "is_active", "name"]


class SalaryStructureVersionViewSet(viewsets.ModelViewSet):
    queryset = SalaryStructureVersion.objects.all().order_by("-effective_from")
    serializer_class = SalaryStructureVersionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["salary_structure", "effective_from", "effective_to"]


class SalaryComponentViewSet(viewsets.ModelViewSet):
    queryset = SalaryComponent.objects.all().order_by("-created_at")
    serializer_class = SalaryComponentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        "company_id",
        "component_type",
        "is_taxable",
        "is_pf_applicable",
        "is_esi_applicable",
        "is_active",
        "name",
    ]


class PayrollFormulaViewSet(viewsets.ModelViewSet):
    queryset = PayrollFormula.objects.all().order_by("-created_at")
    serializer_class = PayrollFormulaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["company_id", "name"]


class SalaryStructureComponentMappingViewSet(viewsets.ModelViewSet):
    queryset = SalaryStructureComponentMapping.objects.all().order_by(
        "display_order", "created_at"
    )
    serializer_class = SalaryStructureComponentMappingSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        "salary_structure_version",
        "salary_component",
        "formula",
        "calculation_type",
    ]