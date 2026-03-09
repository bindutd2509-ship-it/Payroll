from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .models import AuditLog, ApiKey
from .serializers import AuditLogSerializer, ApiKeySerializer

class AuditLogListView(generics.ListAPIView):
    queryset = AuditLog.objects.all()
    serializer_class = AuditLogSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['company', 'user', 'module_name', 'action']

class ApiKeyListCreateView(generics.ListCreateAPIView):
    queryset = ApiKey.objects.all()
    serializer_class = ApiKeySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['company', 'is_active']

class ApiKeyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ApiKey.objects.all()
    serializer_class = ApiKeySerializer
    lookup_field = 'pk'