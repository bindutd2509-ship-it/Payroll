from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
urlpatterns = [
    path("admin/", admin.site.urls),

    # JWT
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    
    # App Endpoints
    path('api/accounts/', include('app.accounts.urls')),
    path('api/companies/', include('app.companies.urls')),
    path('api/employees/', include('app.employees.urls')),
    path('api/salary/', include('app.salary.urls')),
    path('api/organization/', include('app.organization.urls')),
    path('api/leaves/', include('app.leave_management.urls')),
    path('api/attendance/', include('app.attendance_app.urls')),
    path('api/reimbursements/', include('app.reimbursements.urls')),
    path('api/taxation/', include('app.taxation.urls')),
    path('api/loans/', include('app.loans.urls')),
    path('api/payroll-processing/', include('payroll.urls')),
]
