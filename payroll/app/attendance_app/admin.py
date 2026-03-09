from django.contrib import admin
from .models import Shift, OfficeLocation, Attendance


@admin.register(Shift)
class ShiftAdmin(admin.ModelAdmin):
    list_display = ['name', 'company', 'start_time', 'end_time', 'grace_minutes']
    list_filter = ['company']
    readonly_fields = ['id', 'created_at']


@admin.register(OfficeLocation)
class OfficeLocationAdmin(admin.ModelAdmin):
    list_display = ['name', 'company', 'latitude', 'longitude', 'radius_meters']
    list_filter = ['company']
    readonly_fields = ['id']


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['employee', 'date', 'check_in', 'check_out', 'status', 'is_locked']
    list_filter = ['company', 'status', 'date', 'is_locked']
    search_fields = ['employee__first_name', 'employee__employee_code']
    readonly_fields = ['id', 'created_at']