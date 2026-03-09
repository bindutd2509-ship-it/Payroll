from django.urls import path
from .views import (
    CompanyListCreateView, CompanyDetailView,
    CompanySettingsListCreateView, CompanySettingsDetailView,
)

urlpatterns = [
    path('', CompanyListCreateView.as_view(), name='company-list-create'),
    path('<str:pk>/', CompanyDetailView.as_view(), name='company-detail'),
    path('settings/', CompanySettingsListCreateView.as_view(), name='company-settings-list'),
    path('settings/<str:pk>/', CompanySettingsDetailView.as_view(), name='company-settings-detail'),
]