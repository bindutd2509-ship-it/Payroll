
from django.contrib import admin
from .models import Employee, EmployeeDocument


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['employee_code', 'first_name', 'last_name', 'email', 'company', 'department', 'designation', 'employment_status', 'is_active']
    list_filter = ['company', 'department', 'designation', 'employment_status', 'is_active', 'employment_type']
    search_fields = ['first_name', 'last_name', 'email', 'employee_code', 'pan_number']
    readonly_fields = ['id', 'created_at', 'updated_at']
    raw_id_fields = ['reporting_manager']


@admin.register(EmployeeDocument)
class EmployeeDocumentAdmin(admin.ModelAdmin):
    list_display = ['employee', 'document_type', 'uploaded_at']
    list_filter = ['document_type']
    search_fields = ['employee__first_name', 'employee__employee_code']
    readonly_fields = ['id', 'uploaded_at']