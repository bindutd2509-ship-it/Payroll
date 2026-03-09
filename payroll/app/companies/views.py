from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Company, CompanySettings
from .serializers import CompanySerializer, CompanySettingsSerializer


class CompanyListCreateView(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'email']


class CompanyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    lookup_field = 'pk'


class CompanySettingsListCreateView(generics.ListCreateAPIView):
    queryset = CompanySettings.objects.all()
    serializer_class = CompanySettingsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['company']


class CompanySettingsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CompanySettings.objects.all()
    serializer_class = CompanySettingsSerializer
    lookup_field = 'pk'