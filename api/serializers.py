from rest_framework import serializers
from core.models import TailorShop, CustomerInformation, MeasurementType, \
    CustomerMeasurement, Order, OrderMeasurements


class TailorShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = TailorShop
        fields = '__all__'


class MeasurementTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeasurementType
        fields = '__all__'


class OrderMesurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderMeasurements
        fields = '__all__'


class CustomerMeasurementSerializer(serializers.ModelSerializer):
    # measurement_type = MeasurementTypeSerializer(read_only=True)

    class Meta:
        model = CustomerMeasurement
        fields = '__all__'


class CustomerInformationSerializer(serializers.ModelSerializer):
    measurements = serializers.SerializerMethodField()

    class Meta:
        model = CustomerInformation
        fields = '__all__'

    def get_measurements(self, instance):
        measurements_qs = CustomerMeasurement.objects.filter(customer=instance)
        measurements_serializer = CustomerMeasurementSerializer(
            measurements_qs, many=True)
        return measurements_serializer.data


class OrderSerializer(serializers.ModelSerializer):
    instance_measurement = OrderMesurementSerializer(read_only=True)
    measurements_name = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = '__all__'

    def get_measurements_name(self, obj):
        if (obj.measurement_type.name):
            return obj.measurement_type.name
        else:
            return ''
