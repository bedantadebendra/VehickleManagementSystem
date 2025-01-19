from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ComponentViewSet, VehicleViewSet, RepairViewSet, RevenueViewSet

router = DefaultRouter()
router.register('components', ComponentViewSet)
router.register('vehicles', VehicleViewSet)
router.register('repairs', RepairViewSet)
router.register('revenue', RevenueViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
