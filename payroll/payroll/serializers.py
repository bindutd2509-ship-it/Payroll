from rest_framework import serializers
from .models import Payroll, PayrollItem, PayrollItemComponent, Payslip

class PayrollItemComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PayrollItemComponent
        fields = '__all__'
        read_only_fields = ['id']

class PayrollItemSerializer(serializers.ModelSerializer):
    components = PayrollItemComponentSerializer(many=True, read_only=True)
    
    class Meta:
        model = PayrollItem
        fields = '__all__'
        read_only_fields = ['id']

class PayrollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payroll
        fields = '__all__'
        read_only_fields = ['id', 'generated_at', 'generated_by']

class PayslipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payslip
        fields = '__all__'
        read_only_fields = ['id', 'generated_at']