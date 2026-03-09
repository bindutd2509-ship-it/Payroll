from django.contrib import admin
from .models import Loan, LoanRepayment

@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'loan_type', 'principal_amount', 'status', 'start_date')
    list_filter = ('status', 'loan_type', 'start_date')
    search_fields = ('user__email', 'reason')

@admin.register(LoanRepayment)
class LoanRepaymentAdmin(admin.ModelAdmin):
    list_display = ('loan', 'installment_number', 'scheduled_date', 'amount', 'is_paid')
    list_filter = ('is_paid', 'scheduled_date')
