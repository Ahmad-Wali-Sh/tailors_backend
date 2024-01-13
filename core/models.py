from django.db import models

class TailorShop(models.Model):
    name = models.CharField(max_length=255)
    contact = models.CharField(max_length=20)
    address = models.TextField()
    description = models.TextField()
    tailor_name = models.CharField(max_length=255)
    unit = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class CustomerInformation(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    contact = models.CharField(max_length=20)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    measurements = models.ManyToManyField('MeasurementType', through='CustomerMeasurement')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class MeasurementType(models.Model):
    name = models.CharField(max_length=50)
    fields = models.JSONField()

    def __str__(self):
        return self.name

class CustomerMeasurement(models.Model):
    customer = models.ForeignKey(CustomerInformation, on_delete=models.CASCADE)
    measurement_type = models.ForeignKey(MeasurementType, on_delete=models.CASCADE)
    data = models.JSONField()

    def __str__(self):
        return f"{self.customer} - {self.measurement_type}"


class Order(models.Model):
    customer = models.ForeignKey(CustomerInformation, on_delete=models.CASCADE)
    measurement_type = models.ForeignKey(MeasurementType, on_delete=models.CASCADE)
    instance_measurement = models.ForeignKey(CustomerMeasurement, on_delete=models.CASCADE)
    status = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date_delivery = models.DateField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order for {self.customer} - {self.measurement_type}"