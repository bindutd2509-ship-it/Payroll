from django.contrib import admin
from .models import AuditLog, ApiKey

@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display = ['user', 'action', 'module_name', 'timestamp']
    list_filter = ['action', 'module_name', 'company']
    search_fields = ['user__username', 'module_name']
    readonly_fields = ['timestamp']

@admin.register(ApiKey)
class ApiKeyAdmin(admin.ModelAdmin):
    list_display = ['company', 'is_active', 'created_at']
    list_filter = ['is_active', 'company']
    readonly_fields = ['created_at']
