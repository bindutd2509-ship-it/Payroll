from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaxDeclarationViewSet, InvestmentProofViewSet

router = DefaultRouter()
router.register('declarations', TaxDeclarationViewSet)
router.register('proofs', InvestmentProofViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
