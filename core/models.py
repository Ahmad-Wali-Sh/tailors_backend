from django.db import models

class TailorShopInfo(models.Model):
    name = models.CharField(max_length=50)
    contact = models.CharField(max_length=40)
    address = models.TextField(null=True, blank=True)
    description = models.CharField(max_length=50, null=True, blank=True)
    tailor_name = models.CharField(max_length=50, null=True, blank=True)
    unit = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.name

class ClothingType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class CustomField(models.Model):
    clothing_type = models.ForeignKey(ClothingType, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    data_type = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.clothing_type} - {self.name}"

class Measurement(models.Model):
    clothing_type = models.ForeignKey(ClothingType, on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.clothing_type} Measurements"

class CustomFieldValue(models.Model):
    measurement = models.ForeignKey(Measurement, on_delete=models.CASCADE, related_name='custom_fields_values')
    custom_field = models.ForeignKey(CustomField, on_delete=models.CASCADE)
    value_char = models.CharField(max_length=50, null=True, blank=True)
    value_float = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.measurement} - {self.custom_field} Value: {self.value_char} | {self.value_float}"

class CustomerInfo(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    contact = models.CharField(max_length=30, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created = models.DateField(auto_now=True)
    updated = models.DateField(auto_now_add=True)
    measurements = models.ManyToManyField(Measurement, related_name='customer_measurements')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Order(models.Model):
    ORDER_STATUS_CHOICES = [
        ('NEW', 'New'),
        ('COMPLETED', 'Completed'),
        ('PAID', 'Paid'),
    ]

    customer = models.ForeignKey(CustomerInfo, on_delete=models.CASCADE, related_name='orders')
    clothing_type = models.ForeignKey(ClothingType, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_date = models.DateField()
    delivery_date = models.DateField()
    status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES, default='NEW')

    # Add a OneToOneField for Measurement
    measurement = models.OneToOneField(Measurement, on_delete=models.CASCADE, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.pk is None and not self.measurement:  # Check if it's a new instance and measurement field is not already set
            # Automatically create Measurement instance based on customer's existing measurements
            measurement_data = self.customer.measurements.filter(clothing_type=self.clothing_type).first()
            if measurement_data:
                measurement_instance = Measurement.objects.create(
                    clothing_type=self.clothing_type,
                )
                # Copy custom fields from customer's measurement to the order's measurement
                for custom_field_value in measurement_data.custom_fields_values.all():
                    CustomFieldValue.objects.create(
                        measurement=measurement_instance,
                        custom_field=custom_field_value.custom_field,
                        value_char=custom_field_value.value_char,
                        value_float=custom_field_value.value_float,
                    )

                # Associate the newly created Measurement with the Order
                self.measurement = measurement_instance

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Order #{self.id} for {self.customer} - {self.clothing_type}"