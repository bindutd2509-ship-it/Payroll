import uuid
from django.db import models
from app.companies.models import Company
from app.employees.models import Employee
from app.accounts.models import User

class LeaveType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='leave_types')
    
    name = models.CharField(max_length=150)
    yearly_quota = models.IntegerField()
    
    carry_forward_allowed = models.BooleanField(default=False)
    max_carry_forward = models.IntegerField(default=0)
    is_paid_leave = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'leave_types'
        unique_together = [('company', 'name')]

    def __str__(self):
        return f"{self.name} ({self.company.name})"

class LeaveBalance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='leave_balances')
    leave_type = models.ForeignKey(LeaveType, on_delete=models.CASCADE, related_name='balances')
    
    year = models.IntegerField()
    allocated = models.IntegerField()
    used = models.IntegerField(default=0)
    remaining = models.IntegerField()

    class Meta:
        db_table = 'leave_balances'
        unique_together = [('employee', 'leave_type', 'year')]

    def __str__(self):
        return f"{self.employee.first_name} - {self.leave_type.name} ({self.year})"

class LeaveRequest(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='leave_requests')
    leave_type = models.ForeignKey(LeaveType, on_delete=models.CASCADE, related_name='requests')
    
    start_date = models.DateField()
    end_date = models.DateField()
    total_days = models.DecimalField(max_digits=5, decimal_places=2)
    
    status = models.CharField(max_length=50, default='Pending') # Pending, Approved, Rejected, Cancelled
    
    approved_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='approved_leaves')
    approved_at = models.DateTimeField(null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'leave_requests'

    def __str__(self):
        return f"{self.employee.first_name} - {self.start_date} to {self.end_date}"