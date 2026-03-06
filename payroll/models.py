
from django.db import models

class Employee(models.Model):
    
    company_id = models.CharField(max_length=50)
    employee_code = models.CharField(max_length=50)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
    mobile = models.CharField(max_length=20)
    department_id = models.CharField(max_length=50)
    designation_id = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name