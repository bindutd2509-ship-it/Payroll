from django.urls import path
from .views import (
    EmployeeListCreateView, EmployeeDetailView,
    EmployeeDocumentListCreateView, EmployeeDocumentDetailView,
)

urlpatterns = [
    path('', EmployeeListCreateView.as_view(), name='employee-list-create'),
    path('<str:pk>/', EmployeeDetailView.as_view(), name='employee-detail'),
    path('documents/', EmployeeDocumentListCreateView.as_view(), name='employee-doc-list'),
    path('documents/<str:pk>/', EmployeeDocumentDetailView.as_view(), name='employee-doc-detail'),
]