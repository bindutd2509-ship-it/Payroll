from django.contrib import admin
from .models import TaxDeclaration, InvestmentProof

@admin.register(TaxDeclaration)
class TaxDeclarationAdmin(admin.ModelAdmin):
    list_display = ('user', 'financial_year', 'section_code', 'declared_amount', 'status')
    list_filter = ('status', 'financial_year', 'section_code')
    search_fields = ('user__email', 'remarks')

@admin.register(InvestmentProof)
class InvestmentProofAdmin(admin.ModelAdmin):
    list_display = ('declaration', 'uploaded_at', 'is_verified')
    list_filter = ('is_verified', 'uploaded_at')
