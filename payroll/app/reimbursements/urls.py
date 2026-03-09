from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClaimTypeViewSet, ReimbursementClaimViewSet

router = DefaultRouter()
router.register('types', ClaimTypeViewSet)
router.register('claims', ReimbursementClaimViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
