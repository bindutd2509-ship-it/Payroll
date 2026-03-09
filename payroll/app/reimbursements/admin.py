from django.contrib import admin
from .models import ClaimType, ReimbursementClaim

@admin.register(ClaimType)
class ClaimTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'is_active')
    list_filter = ('company', 'is_active')
    search_fields = ('name',)

@admin.register(ReimbursementClaim)
class ReimbursementClaimAdmin(admin.ModelAdmin):
    list_display = ('id', 'employee_user', 'claim_type', 'amount', 'status', 'claim_date')
    list_filter = ('status', 'claim_type', 'claim_date')
    search_fields = ('employee_user__email', 'description')
