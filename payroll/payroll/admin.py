from django.contrib import admin
from .models import Payroll, PayrollItem, PayrollItemComponent, Payslip

@admin.register(Payroll)
class PayrollAdmin(admin.ModelAdmin):
    list_display = ['company', 'month', 'year', 'status', 'total_net']
    list_filter = ['status', 'month', 'year', 'company']
    search_fields = ['company__name']

@admin.register(PayrollItem)
class PayrollItemAdmin(admin.ModelAdmin):
    list_display = ['employee', 'payroll', 'net_salary', 'is_paid']
    list_filter = ['is_paid', 'payroll']
    search_fields = ['employee__first_name', 'employee__employee_code']

@admin.register(PayrollItemComponent)
class PayrollItemComponentAdmin(admin.ModelAdmin):
    list_display = ['payroll_item', 'component_name', 'component_type', 'amount']
    list_filter = ['component_type']

@admin.register(Payslip)
class PayslipAdmin(admin.ModelAdmin):
    list_display = ['payslip_number', 'payroll_item', 'generated_at']
    search_fields = ['payslip_number']