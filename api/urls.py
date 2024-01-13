from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    TailorShopViewSet,
    CustomerInformationViewSet,
    MeasurementTypeViewSet,
    CustomerMeasurementViewSet,
    OrderViewSet
)

router = DefaultRouter()
router.register(r'tailorshops', TailorShopViewSet)
router.register(r'customerinformations', CustomerInformationViewSet)
router.register(r'measurementtypes', MeasurementTypeViewSet)
router.register(r'customermeasurements', CustomerMeasurementViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    # Add any additional paths or views here as needed
]