from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .models import Payroll, PayrollItem, PayrollItemComponent, Payslip
from .serializers import PayrollSerializer, PayrollItemSerializer, PayrollItemComponentSerializer, PayslipSerializer

class PayrollListCreateView(generics.ListCreateAPIView):
    queryset = Payroll.objects.all()
    serializer_class = PayrollSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['company', 'month', 'year', 'status']

class PayrollDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payroll.objects.all()
    serializer_class = PayrollSerializer
    lookup_field = 'pk'

class PayrollItemListCreateView(generics.ListCreateAPIView):
    queryset = PayrollItem.objects.all()
    serializer_class = PayrollItemSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['payroll', 'employee', 'is_paid']

class PayslipListCreateView(generics.ListCreateAPIView):
    queryset = Payslip.objects.all()
    serializer_class = PayslipSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['payroll_item']

class PayslipDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payslip.objects.all()
    serializer_class = PayslipSerializer
    lookup_field = 'pk'