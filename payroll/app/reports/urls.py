from django.urls import path
from .views import (
    AttendanceSummaryAPIView,
    PayrollSummaryAPIView,
    LeaveSummaryAPIView
)

urlpatterns = [
    path('attendance-summary/', AttendanceSummaryAPIView.as_view()),
    path('payroll-summary/', PayrollSummaryAPIView.as_view()),
    path('leave-summary/', LeaveSummaryAPIView.as_view()),
]