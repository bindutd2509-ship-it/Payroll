from django.urls import path
from .views import CreatePayment, VerifyPayment

urlpatterns = [
    path('create-payment/', CreatePayment.as_view()),
    path('verify-payment/', VerifyPayment.as_view()),
]