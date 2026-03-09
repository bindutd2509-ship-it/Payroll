from rest_framework import viewsets
from .models import ClaimType, ReimbursementClaim
from .serializers import ClaimTypeSerializer, ReimbursementClaimSerializer

class ClaimTypeViewSet(viewsets.ModelViewSet):
    queryset = ClaimType.objects.all()
    serializer_class = ClaimTypeSerializer

class ReimbursementClaimViewSet(viewsets.ModelViewSet):
    queryset = ReimbursementClaim.objects.all()
    serializer_class = ReimbursementClaimSerializer

    def perform_create(self, serializer):
        serializer.save(employee_user=self.request.user)
