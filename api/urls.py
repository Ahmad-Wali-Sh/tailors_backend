from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TailorShopInfoViewSet, MeasurementAfghaniViewSet, MeasurementSuitViewSet, CustomerInfoViewSet, OrderStyleAfghaniViewSet, OrderStyleSuitViewSet, OrderViewSet

router = DefaultRouter()
router.register(r'tailor-shop-info', TailorShopInfoViewSet)
router.register(r'measurement-afghani', MeasurementAfghaniViewSet)
router.register(r'measurement-suit', MeasurementSuitViewSet)
router.register(r'customer-info', CustomerInfoViewSet)
router.register(r'order-style-afghani', OrderStyleAfghaniViewSet)
router.register(r'order-style-suit', OrderStyleSuitViewSet)
router.register(r'order', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]