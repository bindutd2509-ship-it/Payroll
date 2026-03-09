from rest_framework import generics
from .models import Department, Designation
from .serializers import DepartmentSerializer, DesignationSerializer


# ── Department Views ──────────────────────────────────────────────────────────

class DepartmentListCreateView(generics.ListCreateAPIView):
    """List all departments or create a new one."""
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    def get_queryset(self):
        qs = Department.objects.all()
        company_id = self.request.query_params.get('company_id')
        if company_id:
            qs = qs.filter(company_id=company_id)
        return qs


class DepartmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, update or delete a department by id."""
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    lookup_field = 'pk'


# ── Designation Views ─────────────────────────────────────────────────────────

class DesignationListCreateView(generics.ListCreateAPIView):
    """List all designations or create a new one."""
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer

    def get_queryset(self):
        qs = Designation.objects.all()
        company_id = self.request.query_params.get('company_id')
        if company_id:
            qs = qs.filter(company_id=company_id)
        return qs


class DesignationDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, update or delete a designation by id."""
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer
    lookup_field = 'pk'