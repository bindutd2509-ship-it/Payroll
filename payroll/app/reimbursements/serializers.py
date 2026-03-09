from rest_framework import serializers
from .models import ClaimType, ReimbursementClaim

class ClaimTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClaimType
        fields = '__all__'

class ReimbursementClaimSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReimbursementClaim
        fields = '__all__'
        read_only_fields = ('status', 'approved_by', 'approved_at', 'rejection_reason')
