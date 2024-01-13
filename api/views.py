from rest_framework import viewsets
from core.models import TailorShop, CustomerInformation, MeasurementType, CustomerMeasurement, Order
from .serializers import (
    TailorShopSerializer,
    CustomerInformationSerializer,
    MeasurementTypeSerializer,
    CustomerMeasurementSerializer,
    OrderSerializer
)

class TailorShopViewSet(viewsets.ModelViewSet):
    queryset = TailorShop.objects.all()
    serializer_class = TailorShopSerializer

class CustomerInformationViewSet(viewsets.ModelViewSet):
    queryset = CustomerInformation.objects.all()
    serializer_class = CustomerInformationSerializer

class MeasurementTypeViewSet(viewsets.ModelViewSet):
    queryset = MeasurementType.objects.all()
    serializer_class = MeasurementTypeSerializer

class CustomerMeasurementViewSet(viewsets.ModelViewSet):
    queryset = CustomerMeasurement.objects.all()
    serializer_class = CustomerMeasurementSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer