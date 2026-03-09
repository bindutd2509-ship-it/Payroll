import uuid
from django.db import models
from app.companies.models import Company
from app.accounts.models import User

class AuditLog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='audit_logs')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='audit_logs')
    
    module_name = models.CharField(max_length=150)
    action = models.CharField(max_length=150) # Create, Update, Delete, Login, etc.
    record_id = models.UUIDField(null=True, blank=True)
    
    old_data = models.TextField(null=True, blank=True)
    new_data = models.TextField(null=True, blank=True)
    
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'audit_logs'

    def __str__(self):
        return f"{self.user} - {self.action} on {self.module_name}"

class ApiKey(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='api_keys')
    
    api_key = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'api_keys'

    def __str__(self):
        return f"API Key for {self.company.name}"