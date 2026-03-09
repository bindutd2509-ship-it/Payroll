from rest_framework import viewsets
from .models import Loan, LoanRepayment
from .serializers import LoanSerializer, LoanRepaymentSerializer

class LoanViewSet(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class LoanRepaymentViewSet(viewsets.ModelViewSet):
    queryset = LoanRepayment.objects.all()
    serializer_class = LoanRepaymentSerializer
