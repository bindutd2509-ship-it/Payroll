from django.db import models
from app.core.models import BaseModel
from app.accounts.models import User

class TaxDeclaration(BaseModel):
    STATUS_CHOICES = (
        ('DRAFT', 'Draft'),
        ('SUBMITTED', 'Submitted'),
        ('VERIFIED', 'Verified'),
        ('REJECTED', 'Rejected'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tax_declarations')
    financial_year = models.CharField(max_length=10) # e.g., 2024-25
    
    section_code = models.CharField(max_length=50) # e.g., 80C, 80D, HRA
    declared_amount = models.DecimalField(max_digits=12, decimal_places=2)
    verified_amount = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='DRAFT')
    remarks = models.TextField(blank=True)

    class Meta:
        db_table = 'tax_declarations'
        unique_together = ('user', 'financial_year', 'section_code')

    def __str__(self):
        return f"{self.user.email} - {self.section_code} ({self.financial_year})"

class InvestmentProof(BaseModel):
    declaration = models.ForeignKey(TaxDeclaration, on_delete=models.CASCADE, related_name='proofs')
    file_path = models.CharField(max_length=500)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)

    class Meta:
        db_table = 'investment_proofs'
