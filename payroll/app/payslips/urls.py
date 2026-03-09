# payroll/urls.py
from django.urls import path
from .views import PayslipCreateAPIView, PayslipListAPIView

urlpatterns = [
    path('payslips/', PayslipListAPIView.as_view(), name='list-payslips'),
    path('payslips/create/', PayslipCreateAPIView.as_view(), name='create-payslip'),
]
