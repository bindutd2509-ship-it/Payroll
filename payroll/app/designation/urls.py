from django.urls import path
from .views import CreateDesignationAPI, ListDesignationAPI

urlpatterns = [
    path('create/', CreateDesignationAPI.as_view()),
    path('list/', ListDesignationAPI.as_view()),
]
