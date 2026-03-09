from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .models import Shift, OfficeLocation, Attendance
from .serializers import ShiftSerializer, OfficeLocationSerializer, AttendanceSerializer


class ShiftListCreateView(generics.ListCreateAPIView):
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['company']


class ShiftDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer
    lookup_field = 'pk'


class OfficeLocationListCreateView(generics.ListCreateAPIView):
    queryset = OfficeLocation.objects.all()
    serializer_class = OfficeLocationSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['company']


class OfficeLocationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OfficeLocation.objects.all()
    serializer_class = OfficeLocationSerializer
    lookup_field = 'pk'


class AttendanceListCreateView(generics.ListCreateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['company', 'employee', 'date', 'status']


class AttendanceCheckInView(generics.CreateAPIView):
    """Check-in endpoint: creates or updates today's attendance record."""
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer


class AttendanceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    lookup_field = 'pk'