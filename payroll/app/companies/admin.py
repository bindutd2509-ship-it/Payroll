from django.contrib import admin
from .models import Company, CompanySettings


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'currency', 'is_active', 'created_at']
    list_filter = ['is_active', 'currency', 'country']
    search_fields = ['name', 'email', 'registration_number']
    readonly_fields = ['id', 'created_at', 'updated_at']


@admin.register(CompanySettings)
class CompanySettingsAdmin(admin.ModelAdmin):
    list_display = ['company', 'payroll_cycle', 'pf_enabled', 'esi_enabled', 'tds_enabled']
    list_filter = ['pf_enabled', 'esi_enabled', 'tds_enabled']
    readonly_fields = ['id', 'created_at']