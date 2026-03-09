from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LoanViewSet, LoanRepaymentViewSet

router = DefaultRouter()
router.register('loans', LoanViewSet)
router.register('repayments', LoanRepaymentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
