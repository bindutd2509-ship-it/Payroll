from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Employee, EmployeeDocument
from .serializers import EmployeeSerializer, EmployeeListSerializer, EmployeeDocumentSerializer


class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.select_related('company', 'department', 'designation').all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['company', 'department', 'designation', 'is_active', 'employment_status']
    search_fields = ['first_name', 'last_name', 'email', 'employee_code']

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return EmployeeListSerializer
        return EmployeeSerializer


class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'pk'


class EmployeeDocumentListCreateView(generics.ListCreateAPIView):
    queryset = EmployeeDocument.objects.all()
    serializer_class = EmployeeDocumentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['employee']


class EmployeeDocumentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EmployeeDocument.objects.all()
    serializer_class = EmployeeDocumentSerializer
    lookup_field = 'pk'