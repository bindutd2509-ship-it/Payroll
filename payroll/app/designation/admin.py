# admin.py

from django.contrib import admin
from .models import Designation


class DesignationAdmin(admin.ModelAdmin):
    list_display = ['id', 'company_id', 'name', 'is_active', 'created_at']


admin.site.register(Designation, DesignationAdmin)