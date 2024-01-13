from rest_framework import viewsets
from core.models import ClothingType, CustomField, Measurement, CustomerInfo, Order, TailorShopInfo
from .serializers import ClothingTypeSerializer, CustomFieldSerializer, MeasurementSerializer, TailorShopInfoSerialzier, CustomerInfoSerializer, OrderSerializer

class TailorShopView(viewsets.ModelViewSet):
    queryset = TailorShopInfo.objects.all()
    serializer_class = TailorShopInfoSerialzier

class ClothingTypeViewSet(viewsets.ModelViewSet):
    queryset = ClothingType.objects.all()
    serializer_class = ClothingTypeSerializer

class CustomFieldViewSet(viewsets.ModelViewSet):
    queryset = CustomField.objects.all()
    serializer_class = CustomFieldSerializer

class MeasurementViewSet(viewsets.ModelViewSet):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

class CustomerInfoViewSet(viewsets.ModelViewSet):
    queryset = CustomerInfo.objects.all()
    serializer_class = CustomerInfoSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer