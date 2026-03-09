from django.urls import path
from .views import (
    ShiftListCreateView, ShiftDetailView,
    OfficeLocationListCreateView, OfficeLocationDetailView,
    AttendanceListCreateView, AttendanceDetailView,
    AttendanceCheckInView,
)

urlpatterns = [
    path('shifts/', ShiftListCreateView.as_view(), name='shift-list'),
    path('shifts/<str:pk>/', ShiftDetailView.as_view(), name='shift-detail'),
    path('office-locations/', OfficeLocationListCreateView.as_view(), name='office-location-list'),
    path('office-locations/<str:pk>/', OfficeLocationDetailView.as_view(), name='office-location-detail'),
    path('', AttendanceListCreateView.as_view(), name='attendance-list'),
    path('check-in/', AttendanceCheckInView.as_view(), name='attendance-checkin'),
    path('<str:pk>/', AttendanceDetailView.as_view(), name='attendance-detail'),
]