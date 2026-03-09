from django.db import models
from app.core.models import BaseModel
from app.accounts.models import User
from app.companies.models import Company

class ClaimType(BaseModel):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='claim_types')
    name = models.CharField(max_length=100) # e.g., Travel, Medical, Broadband
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'claim_types'
        unique_together = ('company', 'name')

    def __str__(self):
        return f"{self.name} ({self.company.name})"

class ReimbursementClaim(BaseModel):
    STATUS_CHOICES = (
        ('DRAFT', 'Draft'),
        ('SUBMITTED', 'Submitted'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
        ('PAID', 'Paid'),
    )

    employee_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='claims')
    claim_type = models.ForeignKey(ClaimType, on_delete=models.PROTECT)
    
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    claim_date = models.DateField()
    description = models.TextField()
    
    receipt_path = models.CharField(max_length=500, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='DRAFT')
    
    approved_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='approved_claims')
    approved_at = models.DateTimeField(null=True, blank=True)
    rejection_reason = models.TextField(blank=True)

    class Meta:
        db_table = 'reimbursement_claims'
        ordering = ['-created_at']

    def __str__(self):
        return f"Claim {self.id} - {self.employee_user.email} - {self.amount}"
