from rest_framework import viewsets, filters
from core.models import TailorShop, CustomerInformation, MeasurementType, \
    CustomerMeasurement, Order, OrderMeasurements
from .serializers import (
    TailorShopSerializer,
    CustomerInformationSerializer,
    MeasurementTypeSerializer,
    CustomerMeasurementSerializer,
    OrderSerializer,
    OrderMesurementSerializer
)


class TailorShopViewSet(viewsets.ModelViewSet):
    queryset = TailorShop.objects.all()
    serializer_class = TailorShopSerializer


class CustomerInformationViewSet(viewsets.ModelViewSet):
    queryset = CustomerInformation.objects.all()
    serializer_class = CustomerInformationSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['first_name', 'last_name', 'id', 'contact', 'description']

class MeasurementTypeViewSet(viewsets.ModelViewSet):
    queryset = MeasurementType.objects.all()
    serializer_class = MeasurementTypeSerializer


class CustomerMeasurementViewSet(viewsets.ModelViewSet):
    queryset = CustomerMeasurement.objects.all()
    serializer_class = CustomerMeasurementSerializer

    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)


class OrderMeasurementViewSet(viewsets.ModelViewSet):
    queryset = OrderMeasurements.objects.all()
    serializer_class = OrderMesurementSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
