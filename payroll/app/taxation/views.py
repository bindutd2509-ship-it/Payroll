from rest_framework import viewsets
from .models import TaxDeclaration, InvestmentProof
from .serializers import TaxDeclarationSerializer, InvestmentProofSerializer

class TaxDeclarationViewSet(viewsets.ModelViewSet):
    queryset = TaxDeclaration.objects.all()
    serializer_class = TaxDeclarationSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class InvestmentProofViewSet(viewsets.ModelViewSet):
    queryset = InvestmentProof.objects.all()
    serializer_class = InvestmentProofSerializer
