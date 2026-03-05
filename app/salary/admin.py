from django.contrib import admin
from .models import SalaryStructure, SalaryStructureVersion, SalaryComponent, PayrollFormula, SalaryStructureComponentMapping, EmployeeSalary, EmployeeSalaryComponentDetail

class EmployeeSalaryComponentDetailInline(admin.TabularInline):
    model = EmployeeSalaryComponentDetail
    extra = 1

@admin.register(EmployeeSalary)
class EmployeeSalaryAdmin(admin.ModelAdmin):
    list_display = ('employee', 'salary_structure_version', 'is_active', 'created_at')
    list_filter = ('is_active', 'salary_structure_version__salary_structure__company_id')
    search_fields = ('employee__employee_code', 'employee__first_name', 'employee__last_name')
    inlines = [EmployeeSalaryComponentDetailInline]

@admin.register(SalaryStructure)
class SalaryStructureAdmin(admin.ModelAdmin):
    list_display = ('name', 'company_id', 'is_active', 'created_at')
    search_fields = ('name',)
    list_filter = ('is_active', 'company_id')

@admin.register(SalaryStructureVersion)
class SalaryStructureVersionAdmin(admin.ModelAdmin):
    list_display = ('salary_structure', 'effective_from', 'effective_to', 'created_at')
    list_filter = ('salary_structure__company_id',)

@admin.register(SalaryComponent)
class SalaryComponentAdmin(admin.ModelAdmin):
    list_display = ('name', 'component_type', 'is_taxable', 'is_active', 'company_id')
    list_filter = ('component_type', 'is_taxable', 'is_active', 'company_id')
    search_fields = ('name',)

@admin.register(PayrollFormula)
class PayrollFormulaAdmin(admin.ModelAdmin):
    list_display = ('name', 'company_id', 'created_at')
    search_fields = ('name',)

@admin.register(SalaryStructureComponentMapping)
class SalaryStructureComponentMappingAdmin(admin.ModelAdmin):
    list_display = ('salary_structure_version', 'salary_component', 'calculation_type', 'value', 'display_order')
    list_filter = ('calculation_type', 'salary_structure_version__salary_structure__company_id')
