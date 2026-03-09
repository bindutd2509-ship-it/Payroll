from django.db import models
from app.core.models import BaseModel
from app.accounts.models import User

class Loan(BaseModel):
    STATUS_CHOICES = (
        ('PENDING', 'Pending Approval'),
        ('ACTIVE', 'Active'),
        ('COMPLETED', 'Completed'),
        ('REJECTED', 'Rejected'),
    )

    LOAN_TYPES = (
        ('HOME', 'Home Loan'),
        ('MEDICAL', 'Medical Loan'),
        ('PERSONAL', 'Personal Loan'),
        ('SALARY_ADVANCE', 'Salary Advance'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='loans')
    loan_type = models.CharField(max_length=50, choices=LOAN_TYPES)
    
    principal_amount = models.DecimalField(max_digits=15, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0.0) # Percentage
    
    tenure_months = models.IntegerField() # Duration in months
    monthly_installment = models.DecimalField(max_digits=12, decimal_places=2)
    
    start_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    
    reason = models.TextField(blank=True)

    class Meta:
        db_table = 'loans'

    def __str__(self):
        return f"Loan {self.id} - {self.user.email} - {self.principal_amount}"

class LoanRepayment(BaseModel):
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE, related_name='repayments')
    installment_number = models.IntegerField()
    scheduled_date = models.DateField()
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    
    is_paid = models.BooleanField(default=False)
    paid_at = models.DateTimeField(null=True, blank=True)
    
    payroll_item = models.ForeignKey('payroll_processing.PayrollItem', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        db_table = 'loan_repayments'
        ordering = ['installment_number']
