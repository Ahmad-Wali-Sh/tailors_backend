from rest_framework import serializers
from core.models import ClothingType, CustomField, Measurement, CustomFieldValue, CustomerInfo, Order, TailorShopInfo

class TailorShopInfoSerialzier(serializers.ModelSerializer):
    class Meta:
        model = TailorShopInfo
        fields = '__all__'

class ClothingTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClothingType
        fields = '__all__'

class CustomFieldSerializer(serializers.ModelSerializer):
    clothing_type = ClothingTypeSerializer()
    class Meta:
        model = CustomField
        fields = '__all__'


class CustomFieldValueSerializer(serializers.ModelSerializer):
    custom_field = CustomFieldSerializer(read_only=True)
    measurement = serializers.PrimaryKeyRelatedField(queryset=Measurement.objects.all())
    class Meta:
        model = CustomFieldValue
        fields = '__all__'

class MeasurementSerializer(serializers.ModelSerializer):
    custom_fields_values = CustomFieldValueSerializer(many=True, read_only=True)
    clothing_type = ClothingTypeSerializer()

    class Meta:
        model = Measurement
        fields = '__all__'


class CustomerInfoSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(many=True, read_only=True)
    class Meta:
        model = CustomerInfo
        fields = '__all__'




class OrderSerializer(serializers.ModelSerializer):
    clothing_type = ClothingTypeSerializer()
    customer = CustomerInfoSerializer()
    measurement = MeasurementSerializer()
    class Meta:
        model = Order
        fields = '__all__'