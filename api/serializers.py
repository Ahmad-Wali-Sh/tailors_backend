from rest_framework import serializers
from core.models import TailorShop, CustomerInformation, MeasurementType, CustomerMeasurement, Order

class TailorShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = TailorShop
        fields = '__all__'

class MeasurementTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeasurementType
        fields = '__all__'

class CustomerMeasurementSerializer(serializers.ModelSerializer):
    measurement_type = MeasurementTypeSerializer(read_only=True)
    class Meta:
        model = CustomerMeasurement
        fields = '__all__'

class CustomerInformationSerializer(serializers.ModelSerializer):
    # measurements = CustomerMeasurementSerializer(many=True, read_only=True)

    class Meta:
        model = CustomerInformation
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'