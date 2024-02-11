from django.db import models


class TailorShop(models.Model):
    name = models.CharField(max_length=60)
    contact = models.CharField(max_length=80)
    address = models.TextField()
    description = models.TextField(null=True, blank=True)
    day_to_deliver = models.PositiveIntegerField(default=3)
    date_to_deliver = models.DateField(null=True, blank=True)
    default_price = models.DecimalField(
        max_digits=10, decimal_places=1, default=350)

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
    required = models.BooleanField(default=True)
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
    customer = models.ForeignKey(CustomerInformation, on_delete=models.CASCADE)
    measurement_type = models.ForeignKey(
        MeasurementType, on_delete=models.CASCADE)
    instance_measurement = models.ForeignKey(
        OrderMeasurements, on_delete=models.CASCADE, null=True, blank=True)
    archieved = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)
    parcha = models.CharField(max_length=60, null=True, blank=True)
    meters = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)

    dokht_price = models.DecimalField(max_digits=10, decimal_places=2)
    clothing_price = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)
    rasid = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    al_baghi = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    grand_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
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

        self.grand_total = self.dokht_price + self.clothing_price
        self.al_baghi = self.grand_total - self.rasid
        super().save(*args, **kwargs)


class ExpenseTypes (models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Expense (models.Model):
    name = models.CharField(max_length=120)
    quantity = models.CharField(max_length=60, null=True, blank=True)
    price = models.FloatField()
    type = models.ForeignKey(
        ExpenseTypes, on_delete=models.CASCADE, null=True, blank=True)
    paid = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Receivables (models.Model):
    customer = models.OneToOneField(
        CustomerInformation, on_delete=models.CASCADE)
    reason = models.CharField(max_length=255)
    price = models.FloatField()
    paid = models.BooleanField(default=False)
