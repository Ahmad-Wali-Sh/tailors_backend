from django.contrib import admin
from .models import TailorShopInfo, MeasurementAfghani, MeasurementSuit, CustomerInfo, OrderStyleAfghani, OrderStyleSuit, Order

@admin.register(TailorShopInfo)
class TailorShopInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact', 'email', 'telegram', 'tailor_name', 'unit')
    search_fields = ('name', 'contact', 'email', 'tailor_name')

@admin.register(MeasurementAfghani)
class MeasurementAfghaniAdmin(admin.ModelAdmin):
    list_display = ('qad', 'astin', 'shana', 'yakhan', 'baghal', 'bardaman', 'pants_qad', 'pants_dam', 'created', 'updated')
    search_fields = ('created',)

@admin.register(MeasurementSuit)
class MeasurementSuitAdmin(admin.ModelAdmin):
    pass

@admin.register(CustomerInfo)
class CustomerInfoAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'contact', 'created', 'updated')
    search_fields = ('first_name', 'last_name', 'contact')

@admin.register(OrderStyleAfghani)
class OrderStyleAfghaniAdmin(admin.ModelAdmin):
    list_display = ('model_daman', 'model_astin', 'model_dokma', 'model_yakhan', 'model_bartaman', 'kisa_ro', 'kisa_taman', 'clothing_description')

@admin.register(OrderStyleSuit)
class OrderStyleSuitAdmin(admin.ModelAdmin):
    pass

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'style_afghani', 'style_suit', 'order_date', 'delivery_date', 'total_price', 'completed')
    search_fields = ('customer__first_name', 'customer__last_name', 'order_date', 'delivery_date')