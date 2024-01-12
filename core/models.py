from django.db import models

class TailorShopInfo(models.Model):
    name = models.CharField(max_length=50)
    contact = models.CharField(max_length=40)
    address = models.TextField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    telegram = models.CharField(max_length=50, null=True, blank=True)
    tailor_name = models.CharField(max_length=50, null=True, blank=True)
    unit = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.name

class MeasurementAfghani(models.Model):
    qad = models.FloatField()
    astin = models.FloatField()
    shana = models.FloatField()
    yakhan = models.FloatField()
    baghal = models.FloatField()
    bardaman = models.FloatField()
    pants_qad = models.FloatField()
    pants_dam = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class MeasurementSuit(models.Model):
    # Placeholder for suit measurements; add specific fields as needed
    pass

class CustomerInfo(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    contact = models.CharField(max_length=30, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    measurement_afghani = models.OneToOneField(MeasurementAfghani, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='customer_measurement_afghani')
    measurement_suit = models.OneToOneField(MeasurementSuit, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='customer_measurement_suit')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class OrderStyleAfghani(models.Model):
    model_daman = models.CharField(max_length=30)
    model_astin = models.CharField(max_length=30)
    model_dokma = models.CharField(max_length=30)
    model_yakhan = models.CharField(max_length=30)
    model_bartaman = models.CharField(max_length=30)
    clothing_description = models.TextField(null=True, blank=True)
    kisa_ro = models.CharField(max_length=20)
    kisa_taman = models.CharField(max_length=20)

class OrderStyleSuit(models.Model):
    # Placeholder for suit order style; add specific fields as needed
    pass

class Order(models.Model):
    customer = models.ForeignKey(CustomerInfo, on_delete=models.CASCADE, related_name='orders')
    style_afghani = models.OneToOneField(OrderStyleAfghani, on_delete=models.CASCADE, null=True, blank=True, related_name='order_style_afghani')
    style_suit = models.OneToOneField(OrderStyleSuit, on_delete=models.CASCADE, null=True, blank=True, related_name='order_style_suit')
    order_date = models.DateField()
    delivery_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    completed = models.BooleanField(default=False)