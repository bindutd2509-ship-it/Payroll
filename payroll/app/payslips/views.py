from django.shortcuts import render

# Create your views here.
# payroll/views.py
from rest_framework import generics
from .models import Payslip
from .serializers import PayslipSerializer

# Create Payslip
class PayslipCreateAPIView(generics.CreateAPIView):
    queryset = Payslip.objects.all()
    serializer_class = PayslipSerializer

# List Payslips
class PayslipListAPIView(generics.ListAPIView):
    queryset = Payslip.objects.all()
    serializer_class = PayslipSerializer
