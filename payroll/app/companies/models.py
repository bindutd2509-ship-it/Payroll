import uuid
from django.db import models


class Company(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    name = models.CharField(max_length=200)
    legal_name = models.CharField(max_length=200, blank=True)
    registration_number = models.CharField(max_length=100, unique=True, blank=True)
    pan_number = models.CharField(max_length=20, blank=True)
    tan_number = models.CharField(max_length=20, blank=True)
    pf_number = models.CharField(max_length=50, blank=True)
    esi_number = models.CharField(max_length=50, blank=True)
    professional_tax_number = models.CharField(max_length=50, blank=True)

    email = models.EmailField(max_length=200, unique=True)
    phone = models.CharField(max_length=20, blank=True)

    address = models.TextField(blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    pincode = models.CharField(max_length=20, blank=True)

    timezone = models.CharField(max_length=50, default='UTC')
    currency = models.CharField(max_length=10, default='INR')

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'companies'
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.name


class CompanySettings(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company = models.OneToOneField(Company, on_delete=models.CASCADE, related_name='settings')

    financial_year_start_month = models.IntegerField(default=4)
    payroll_cycle = models.CharField(max_length=50, default='Monthly')

    pf_enabled = models.BooleanField(default=False)
    esi_enabled = models.BooleanField(default=False)
    professional_tax_enabled = models.BooleanField(default=False)
    tds_enabled = models.BooleanField(default=False)
    attendance_enabled = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'company_settings'
        verbose_name_plural = 'Company Settings'

    def __str__(self):
        return f"Settings for {self.company.name}"