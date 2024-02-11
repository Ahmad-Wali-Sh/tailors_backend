from django.contrib import admin
from .models import TailorShop, CustomerInformation, MeasurementType, \
    CustomerMeasurement, Order, OrderMeasurements, Expense, Receivables, \
    ExpenseTypes


@admin.register(TailorShop)
class TailorShopAdmin(admin.ModelAdmin):
    list_display = ['name', 'contact']


@admin.register(CustomerInformation)
class CustomerInformationAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'contact', 'created', 'updated']
    search_fields = ['first_name', 'last_name', 'contact']


@admin.register(MeasurementType)
class MeasurementTypeAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(CustomerMeasurement)
class CustomerMeasurementAdmin(admin.ModelAdmin):
    list_display = ['customer', 'measurement_type']
    search_fields = ['customer__first_name',
                     'customer__last_name', 'measurement_type__name']


@admin.register(OrderMeasurements)
class OrderMeasurementsAdmin(admin.ModelAdmin):
    list_display = ['customer', 'measurement_type']
    search_fields = ['customer__first_name',
                     'customer__last_name', 'measurement_type__name']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'measurement_type', 'instance_measurement',
                    'archieved', 'dokht_price', 'date_delivery', 'date_created']
    search_fields = ['customer__first_name',
                     'customer__last_name', 'measurement_type__name']


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'price', 'type',
                    'paid', 'created', 'updated')
    list_filter = ('type', 'paid', 'created', 'updated')
    search_fields = ('name', 'type', 'created')
    date_hierarchy = 'created'


@admin.register(Receivables)
class ReceivablesAdmin(admin.ModelAdmin):
    list_display = ('customer', 'reason', 'price', 'paid')
    search_fields = ('customer__name', 'reason', 'paid')


@admin.register(ExpenseTypes)
class ExpenseTypesAdmin(admin.ModelAdmin):
    list_display = ('name',)
