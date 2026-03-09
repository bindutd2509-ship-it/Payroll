from rest_framework import serializers
from .models import Employee, EmployeeDocument


class EmployeeDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeDocument
        fields = '__all__'
        read_only_fields = ['id', 'uploaded_at']


class EmployeeSerializer(serializers.ModelSerializer):
    documents = EmployeeDocumentSerializer(many=True, read_only=True)

    class Meta:
        model = Employee
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']


class EmployeeListSerializer(serializers.ModelSerializer):
    """Lighter serializer for list endpoints."""
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = Employee
        fields = ['id', 'employee_code', 'full_name', 'email', 'department', 'designation', 'employment_status', 'is_active']

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}".strip()