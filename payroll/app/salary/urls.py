from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
    SalaryStructureViewSet,
    SalaryStructureVersionViewSet,
    SalaryComponentViewSet,
    PayrollFormulaViewSet,
    SalaryStructureComponentMappingViewSet,
)
from .views_payroll import RunPayrollAPIView

router = DefaultRouter()
router.register(r"salary-structures", SalaryStructureViewSet, basename="salary-structures")
router.register(r"salary-structure-versions", SalaryStructureVersionViewSet, basename="salary-structure-versions")
router.register(r"salary-components", SalaryComponentViewSet, basename="salary-components")
router.register(r"payroll-formulas", PayrollFormulaViewSet, basename="payroll-formulas")
router.register(r"salary-structure-component-mappings", SalaryStructureComponentMappingViewSet, basename="salary-structure-component-mappings")

urlpatterns = router.urls + [
    path("payrolls/run/", RunPayrollAPIView.as_view(), name="run-payroll"),
]