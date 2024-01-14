from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    TailorShopViewSet,
    CustomerInformationViewSet,
    MeasurementTypeViewSet,
    CustomerMeasurementViewSet,
    OrderViewSet,
    OrderMeasurementViewSet
)

router = DefaultRouter()
router.register(r'tailorshop', TailorShopViewSet)
router.register(r'customers', CustomerInformationViewSet)
router.register(r'measurement-types', MeasurementTypeViewSet)
router.register(r'customer-measurements', CustomerMeasurementViewSet)
router.register(r'order-mesurements', OrderMeasurementViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    # Add any additional paths or views here as needed
]
