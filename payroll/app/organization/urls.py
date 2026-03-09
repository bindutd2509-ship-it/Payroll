from django.urls import path
from .views import (
    DepartmentListCreateView,
    DepartmentDetailView,
    DesignationListCreateView,
    DesignationDetailView,
)

urlpatterns = [
    # Department endpoints
    path('departments/', DepartmentListCreateView.as_view(), name='department-list-create'),
    path('departments/<str:pk>/', DepartmentDetailView.as_view(), name='department-detail'),

    # Designation endpoints
    path('designations/', DesignationListCreateView.as_view(), name='designation-list-create'),
    path('designations/<str:pk>/', DesignationDetailView.as_view(), name='designation-detail'),
]