from django.db import models

# Create your models here.
# payroll/models.py
import uuid
from django.db import models

class Payslip(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    payroll_item_id = models.UUIDField(unique=True)  # reference to payroll_items.id
    payslip_number = models.CharField(max_length=150)
    file_path = models.CharField(max_length=500)  # path to file
    generated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payslip {self.payslip_number}"
