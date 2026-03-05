from django.urls import path
from .views import (
    PayrollListCreateView, PayrollDetailView,
    PayrollItemListCreateView,
    PayslipListCreateView, PayslipDetailView,
)

urlpatterns = [
    path('', PayrollListCreateView.as_view(), name='payroll-list'),
    path('items/', PayrollItemListCreateView.as_view(), name='payroll-item-list'),
    path('<str:pk>/', PayrollDetailView.as_view(), name='payroll-detail'),
    path('payslips/', PayslipListCreateView.as_view(), name='payslip-list'),
    path('payslips/<str:pk>/', PayslipDetailView.as_view(), name='payslip-detail'),
]