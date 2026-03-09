

# Register your models here.
# admin.py

from django.contrib import admin
from .models import Payslip


class PayslipAdmin(admin.ModelAdmin):
    list_display = ['id','payslip_number', 'payroll_item_id', 'file_path', 'generated_at']


admin.site.register(Payslip, PayslipAdmin)