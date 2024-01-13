from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClothingTypeViewSet, CustomFieldViewSet, TailorShopView, MeasurementViewSet, CustomerInfoViewSet, OrderViewSet

router = DefaultRouter()
router.register(r'clothing-types', ClothingTypeViewSet, basename='clothing-type')
router.register(r'custom-fields', CustomFieldViewSet, basename='custom-field')
router.register(r'tailors-info', TailorShopView, basename='custom-field')
router.register(r'measurements', MeasurementViewSet, basename='measurement')
router.register(r'customer-infos', CustomerInfoViewSet, basename='customer-info')
router.register(r'orders', OrderViewSet, basename='order')

urlpatterns = [
    path('api/', include(router.urls)),
]