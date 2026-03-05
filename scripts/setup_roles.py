import os
import sys
import django

# Add the project root to sys.path
sys.path.append(os.getcwd())

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'employee_project.settings')
django.setup()

from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model

User = get_user_model()

def setup_rbac():
    # 1. Platform Admin Group (Multi-tenancy setup)
    # Scope: Companies and Company Settings
    platform_group, _ = Group.objects.get_or_create(name='Platform Admins')
    platform_apps = ['companies']
    platform_perms = Permission.objects.filter(content_type__app_label__in=platform_apps)
    platform_group.permissions.set(platform_perms)
    print("Platform Admin group created/updated (Companies & Settings).")

    # 2. Operations Admin Group (Employee Lifecycle)
    # Scope: Employees, Attendance, Leave, Organization
    ops_group, _ = Group.objects.get_or_create(name='Operations Admins')
    ops_apps = ['employees', 'attendance_app', 'leave_management', 'organization']
    ops_perms = Permission.objects.filter(content_type__app_label__in=ops_apps)
    ops_group.permissions.set(ops_perms)
    print("Operations Admin group created/updated (Employees, Attendance, Leave, Org).")

    # 3. HR Admin Group (Financials & Payroll)
    # Scope: Payroll, Loans, Taxation, Reimbursements
    hr_group, _ = Group.objects.get_or_create(name='HR Admins')
    hr_apps = ['salary', 'loans', 'taxation', 'reimbursements', 'payroll_processing']
    hr_perms = Permission.objects.filter(content_type__app_label__in=hr_apps)
    hr_group.permissions.set(hr_perms)
    print("HR Admin group created/updated (Payroll, Loans, Tax, Claims).")

    # 4. Create Sample Users
    def create_admin_user(email, username, group, password='admin123'):
        user, created = User.objects.get_or_create(
            email=email,
            defaults={'username': username, 'is_staff': True}
        )
        if created:
            user.set_password(password)
            user.save()
        user.groups.clear() # Clear existing groups to reset
        user.groups.add(group)
        print(f"User {email} created/updated and assigned to {group.name}.")
        return user

    create_admin_user('platform@payroll.com', 'platform_admin', platform_group)
    create_admin_user('ops@payroll.com', 'ops_admin', ops_group)
    create_admin_user('hr@payroll.com', 'hr_admin', hr_group)

if __name__ == "__main__":
    setup_rbac()
