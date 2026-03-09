from django.urls import path
from .views import (
    LeaveTypeListCreateView, LeaveTypeDetailView,
    LeaveBalanceListCreateView,
    LeaveRequestListCreateView, LeaveRequestDetailView,
)

urlpatterns = [
    path('types/', LeaveTypeListCreateView.as_view(), name='leave-type-list'),
    path('types/<str:pk>/', LeaveTypeDetailView.as_view(), name='leave-type-detail'),
    path('balances/', LeaveBalanceListCreateView.as_view(), name='leave-balance-list'),
    path('requests/', LeaveRequestListCreateView.as_view(), name='leave-request-list'),
    path('requests/<str:pk>/', LeaveRequestDetailView.as_view(), name='leave-request-detail'),
]