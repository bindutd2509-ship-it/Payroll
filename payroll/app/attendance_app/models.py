import uuid
from django.db import models
from app.companies.models import Company
from app.employees.models import Employee


class Shift(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='shifts')

    name = models.CharField(max_length=150)
    start_time = models.TimeField()
    end_time = models.TimeField()
    grace_minutes = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'shifts'

    def __str__(self):
        return f"{self.name} ({self.company.name})"


class OfficeLocation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='office_locations')

    name = models.CharField(max_length=150)
    latitude = models.DecimalField(max_digits=10, decimal_places=7)
    longitude = models.DecimalField(max_digits=10, decimal_places=7)
    radius_meters = models.IntegerField(default=100)

    class Meta:
        db_table = 'office_locations'

    def __str__(self):
        return f"{self.name} ({self.company.name})"


class Attendance(models.Model):
    STATUS_CHOICES = [
        ('Present', 'Present'),
        ('Absent', 'Absent'),
        ('Half Day', 'Half Day'),
        ('Late', 'Late'),
        ('On Leave', 'On Leave'),
        ('Holiday', 'Holiday'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='attendance_records')
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='attendance_records')

    shift = models.ForeignKey(Shift, on_delete=models.SET_NULL, null=True, blank=True, related_name='attendance_records')
    location = models.ForeignKey(OfficeLocation, on_delete=models.SET_NULL, null=True, blank=True, related_name='attendance_records')

    date = models.DateField()
    check_in = models.DateTimeField(null=True, blank=True)
    check_out = models.DateTimeField(null=True, blank=True)

    break_minutes = models.IntegerField(default=0)
    total_work_minutes = models.IntegerField(default=0)
    overtime_minutes = models.IntegerField(default=0)

    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Present')
    is_locked = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'attendance'
        unique_together = [('employee', 'date')]

    def __str__(self):
        return f"{self.employee} - {self.date}"