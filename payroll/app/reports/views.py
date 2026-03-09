from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Sum, Count, Q

from attendance.models import Attendance
from pay_roll.models import Payroll
from leave_management.models import Leave

# 1️⃣ Attendance Summary API
class AttendanceSummaryAPIView(APIView):

    def get(self, request):
        month = request.GET.get("month")
        year = request.GET.get("year")

        queryset = Attendance.objects.all()

        if month and year:
            queryset = queryset.filter(
                date__month=month,
                date__year=year
            )

        summary = queryset.aggregate(
            total_present=Count('id', filter=Q(status='P')),
            total_absent=Count('id', filter=Q(status='A')),
            total_leave=Count('id', filter=Q(status='L'))
        )

        return Response({
            "total_present": summary["total_present"] or 0,
            "total_absent": summary["total_absent"] or 0,
            "total_leave": summary["total_leave"] or 0,
        }, status=status.HTTP_200_OK)
# 2️⃣ Payroll Summary API

class PayrollSummaryAPIView(APIView):

    def get(self, request):
        month = request.GET.get("month")
        year = request.GET.get("year")

        queryset = Payroll.objects.all()

        if month and year:
            queryset = queryset.filter(month=month, year=year)

        summary = queryset.aggregate(
            total_basic_salary=Sum('basic_salary'),
            total_deductions=Sum('deductions')
        )

        total_basic = summary["total_basic_salary"] or 0
        total_deductions = summary["total_deductions"] or 0
        total_net_salary = total_basic - total_deductions

        return Response({
            "total_basic_salary": total_basic,
            "total_deductions": total_deductions,
            "total_net_salary": total_net_salary
        }, status=status.HTTP_200_OK)

# 3️⃣ Leave Summary API
class LeaveSummaryAPIView(APIView):

    def get(self, request):
        year = request.GET.get("year")

        queryset = Leave.objects.all()

        if year:
            queryset = queryset.filter(from_date__year=year)

        summary = queryset.aggregate(
            approved=Count('id', filter=Q(status='APPROVED')),
            pending=Count('id', filter=Q(status='PENDING')),
            rejected=Count('id', filter=Q(status='REJECTED'))
        )

        return Response({
            "approved_leaves": summary["approved"] or 0,
            "pending_leaves": summary["pending"] or 0,
            "rejected_leaves": summary["rejected"] or 0
        }, status=status.HTTP_200_OK)