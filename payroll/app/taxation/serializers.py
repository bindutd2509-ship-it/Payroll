from rest_framework import serializers
from .models import TaxDeclaration, InvestmentProof

class TaxDeclarationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaxDeclaration
        fields = '__all__'
        read_only_fields = ('verified_amount', 'status')

class InvestmentProofSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvestmentProof
        fields = '__all__'
