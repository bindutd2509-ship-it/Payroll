# payroll/serializers.py
from rest_framework import serializers
from .models import Payslip

class PayslipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payslip
        fields = '__all__'
        read_only_fields = ('id', 'generated_at')
