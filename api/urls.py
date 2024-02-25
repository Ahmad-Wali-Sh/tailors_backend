from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    TailorShopViewSet,
    CustomerInformationViewSet,
    MeasurementTypeViewSet,
    CustomerMeasurementViewSet,
    OrderViewSet,
    OrderMeasurementViewSet,
    ExpenseViewSet,
    ReceivablesViewSet,
    ExpenseTypesViewSet,
    OrderReportViewSet,
    PrintFormViewSet
)

router = DefaultRouter()
router.register(r'tailorshop', TailorShopViewSet)
router.register(r'customers', CustomerInformationViewSet)
router.register(r'measurement-types', MeasurementTypeViewSet)
router.register(r'customer-measurements', CustomerMeasurementViewSet)
router.register(r'order-mesurements', OrderMeasurementViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'expense', ExpenseViewSet)
router.register(r'recievebles', ReceivablesViewSet)
router.register(r'expense-type', ExpenseTypesViewSet)
router.register(r'orders-report', OrderReportViewSet)
router.register(r'print-form', PrintFormViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
    # Add any additional paths or views here as needed
]
