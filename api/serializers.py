from rest_framework import serializers
from core.models import TailorShopInfo, MeasurementAfghani, MeasurementSuit, CustomerInfo, OrderStyleAfghani, OrderStyleSuit, Order

class TailorShopInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TailorShopInfo
        fields = '__all__'

class MeasurementAfghaniSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeasurementAfghani
        fields = '__all__'

class MeasurementSuitSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeasurementSuit
        fields = '__all__'

class CustomerInfoSerializer(serializers.ModelSerializer):
    measurement_afghani = MeasurementAfghaniSerializer()
    measurement_suit = MeasurementSuitSerializer()

    class Meta:
        model = CustomerInfo
        fields = '__all__'

class OrderStyleAfghaniSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderStyleAfghani
        fields = '__all__'

class OrderStyleSuitSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderStyleSuit
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    customer = CustomerInfoSerializer()
    style_afghani = OrderStyleAfghaniSerializer()
    style_suit = OrderStyleSuitSerializer()

    class Meta:
        model = Order
        fields = '__all__'