from django.db import models


class TailorShop(models.Model):
    name = models.CharField(max_length=60)
    contact = models.CharField(max_length=80)
    address = models.TextField()
    description = models.TextField(null=True, blank=True)
    tailor_name = models.CharField(max_length=60, null=True, blank=True)
    unit = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name


class CustomerInformation(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    contact = models.CharField(max_length=80)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    measurements = models.ManyToManyField(
        'MeasurementType', through='CustomerMeasurement')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class MeasurementType(models.Model):
    name = models.CharField(max_length=50)
    fields = models.JSONField()

    def __str__(self):
        return self.name


class CustomerMeasurement(models.Model):
    customer = models.ForeignKey(CustomerInformation, on_delete=models.CASCADE)
    measurement_type = models.ForeignKey(
        MeasurementType, on_delete=models.CASCADE)
    data = models.JSONField()

    class Meta:
        unique_together = ['customer', 'measurement_type']

    def __str__(self):
        return f"{self.customer} - {self.measurement_type}"


class OrderMeasurements(models.Model):
    customer = models.ForeignKey(CustomerInformation, on_delete=models.CASCADE)
    measurement_type = models.ForeignKey(
        MeasurementType, on_delete=models.CASCADE)
    data = models.JSONField()

    def __str__(self):
        return f"{self.customer} - {self.measurement_type}"


class Order(models.Model):
    STATUS_CHOICES = [
        ('new', 'New'),
        ('completed', 'Completed'),
        ('paid', 'Paid'),
        ('canceled', 'Canceled'),
    ]

    customer = models.ForeignKey(CustomerInformation, on_delete=models.CASCADE)
    measurement_type = models.ForeignKey(
        MeasurementType, on_delete=models.CASCADE)
    instance_measurement = models.ForeignKey(
        OrderMeasurements, on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date_delivery = models.DateField()
    date_created = models.DateField()

    def __str__(self):
        return f"Order for {self.customer} - {self.measurement_type}"

    def save(self, *args, **kwargs):
        fields_data = CustomerMeasurement.objects.filter(
                measurement_type=self.measurement_type) \
                    .filter(customer=self.customer).first()
        new_measurement_instance = OrderMeasurements.objects.create(
                customer=self.customer,
                measurement_type=self.measurement_type,
                data=fields_data.data
            )
        self.instance_measurement = new_measurement_instance
        super().save(*args, **kwargs)
