from rest_framework import serializers
from .models import (
    SalaryStructure,
    SalaryStructureVersion,
    SalaryComponent,
    PayrollFormula,
    SalaryStructureComponentMapping,
)
from rest_framework import serializers


class RunPayrollRequestSerializer(serializers.Serializer):
    company_id = serializers.UUIDField()
    month = serializers.IntegerField(min_value=1, max_value=12)
    year = serializers.IntegerField(min_value=1900, max_value=2200)


class SalaryStructureSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalaryStructure
        fields = "__all__"


class SalaryStructureVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalaryStructureVersion
        fields = "__all__"


class SalaryComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalaryComponent
        fields = "__all__"


class PayrollFormulaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PayrollFormula
        fields = "__all__"


class SalaryStructureComponentMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalaryStructureComponentMapping
        fields = "__all__"