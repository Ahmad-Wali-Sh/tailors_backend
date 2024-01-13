from django.contrib import admin
from .models import TailorShopInfo, ClothingType, CustomField, Measurement, CustomFieldValue, CustomerInfo, Order


class TailorShopInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact', 'address', 'description', 'tailor_name', 'unit')

class ClothingTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)

class CustomFieldAdmin(admin.ModelAdmin):
    list_display = ('name', 'clothing_type', 'data_type')

class MeasurementAdmin(admin.ModelAdmin):
    list_display = ('clothing_type', 'created_date', 'updated_date')
    search_fields = ['clothing_type__name']

class CustomFieldValueAdmin(admin.ModelAdmin):
    list_display = ('measurement','value_char', 'value_float')
    list_filter = ('measurement__clothing_type',)

class CustomerInfoAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'contact', 'created', 'updated')
    search_fields = [ 'first_name', 'last_name']

class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'clothing_type', 'price', 'created_date', 'delivery_date', 'status')
    search_fields = ['clothing_type__name']
    list_filter = ('status', 'clothing_type')

admin.site.register(TailorShopInfo, TailorShopInfoAdmin)
admin.site.register(ClothingType, ClothingTypeAdmin)
admin.site.register(CustomField, CustomFieldAdmin)
admin.site.register(Measurement, MeasurementAdmin)
admin.site.register(CustomFieldValue, CustomFieldValueAdmin)
admin.site.register(CustomerInfo, CustomerInfoAdmin)
admin.site.register(Order, OrderAdmin)