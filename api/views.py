from rest_framework import viewsets, filters
from core.models import TailorShop, CustomerInformation, MeasurementType, \
    CustomerMeasurement, Order, OrderMeasurements, Expense, Receivables, \
    ExpenseTypes
from .serializers import (
    TailorShopSerializer,
    CustomerInformationSerializer,
    MeasurementTypeSerializer,
    CustomerMeasurementSerializer,
    OrderSerializer,
    OrderMesurementSerializer,
    ExpenseSerializer,
    ReceivablesSerializer,
    ExppenseTypesSerializer
)
from django_filters import rest_framework as dfilters
from django_filters.widgets import RangeWidget
from rest_framework.response import Response
from django.db.models import Sum


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


class OrderFilter(dfilters.FilterSet):
    date_delivery = dfilters.DateFromToRangeFilter(
        widget=RangeWidget(attrs={'type': 'date'}))

    class Meta:
        model = Order
        fields = ['customer', 'date_delivery',
                  'measurement_type', 'archieved', 'date_created']


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = (dfilters.DjangoFilterBackend, filters.OrderingFilter)
    filterset_class = OrderFilter
    ordering_fields = ['id', 'date_delivery']
    ordering = ['id', 'date_delivery']


class OrderReportViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = (dfilters.DjangoFilterBackend, filters.OrderingFilter)
    filterset_fields = ['archieved',]

    def list(self, request):
        start_date = request.query_params.get('start_date', None)
        end_date = request.query_params.get('end_date', None)
        archieved = request.query_params.get('archieved', None)

        queryset = Order.objects.all()
        if start_date and end_date:
            queryset = queryset.filter(
                date_created__gte=start_date, date_created__lte=end_date)
        if archieved is not None:
            queryset = queryset.filter(archieved=archieved)

        total_order = queryset.count()
        total_clothing = queryset.aggregate(Sum('clothing_price'))[
            'clothing_price__sum'] or 0
        total_dokht = queryset.aggregate(Sum('dokht_price'))[
            'dokht_price__sum'] or 0
        total_price = queryset.aggregate(Sum('grand_total'))[
            'grand_total__sum'] or 0

        data = {
            'total_order': total_order,
            'total_price': total_price,
            'total_clothing': total_clothing,
            'total_dokht': total_dokht
        }
        return Response(data)


class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer


class ReceivablesViewSet(viewsets.ModelViewSet):
    queryset = Receivables.objects.all()
    serializer_class = ReceivablesSerializer


class ExpenseTypesViewSet(viewsets.ModelViewSet):
    queryset = ExpenseTypes.objects.all()
    serializer_class = ExppenseTypesSerializer
