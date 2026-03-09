from django.urls import path
from .views import (
    AuditLogListView,
    ApiKeyListCreateView, ApiKeyDetailView,
)

urlpatterns = [
    path('logs/', AuditLogListView.as_view(), name='audit-log-list'),
    path('keys/', ApiKeyListCreateView.as_view(), name='api-key-list'),
    path('keys/<str:pk>/', ApiKeyDetailView.as_view(), name='api-key-detail'),
]