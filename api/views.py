from rest_framework import viewsets
from core.models import TailorShopInfo, MeasurementAfghani, MeasurementSuit, CustomerInfo, OrderStyleAfghani, OrderStyleSuit, Order
from .serializers import TailorShopInfoSerializer, MeasurementAfghaniSerializer, MeasurementSuitSerializer, CustomerInfoSerializer, OrderStyleAfghaniSerializer, OrderStyleSuitSerializer, OrderSerializer

class TailorShopInfoViewSet(viewsets.ModelViewSet):
    queryset = TailorShopInfo.objects.all()
    serializer_class = TailorShopInfoSerializer

class MeasurementAfghaniViewSet(viewsets.ModelViewSet):
    queryset = MeasurementAfghani.objects.all()
    serializer_class = MeasurementAfghaniSerializer

class MeasurementSuitViewSet(viewsets.ModelViewSet):
    queryset = MeasurementSuit.objects.all()
    serializer_class = MeasurementSuitSerializer

class CustomerInfoViewSet(viewsets.ModelViewSet):
    queryset = CustomerInfo.objects.all()
    serializer_class = CustomerInfoSerializer

class OrderStyleAfghaniViewSet(viewsets.ModelViewSet):
    queryset = OrderStyleAfghani.objects.all()
    serializer_class = OrderStyleAfghaniSerializer

class OrderStyleSuitViewSet(viewsets.ModelViewSet):
    queryset = OrderStyleSuit.objects.all()
    serializer_class = OrderStyleSuitSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer