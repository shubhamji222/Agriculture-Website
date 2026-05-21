from django.db import models


class Federation(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Farmer(models.Model):
    name = models.CharField(max_length=150)
    village = models.CharField(max_length=150)
    mobile = models.CharField(max_length=20)
    federation = models.ForeignKey(Federation, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


class FarmerPayment(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    method = models.CharField(max_length=80)
    status = models.CharField(max_length=60, default='Pending')

    def __str__(self):
        return f'{self.farmer.name} - {self.amount}'


class Procurement(models.Model):
    product = models.CharField(max_length=120)
    quantity = models.PositiveIntegerField()
    source = models.CharField(max_length=150)
    date = models.DateField()
    notes = models.TextField(blank=True)

    def __str__(self):
        return f'{self.product} ({self.quantity})'


class Purchase(models.Model):
    order_id = models.CharField(max_length=80)
    supplier = models.CharField(max_length=150)
    product = models.CharField(max_length=120)
    quantity = models.PositiveIntegerField()
    cost = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateField()
    payment_status = models.CharField(max_length=80, default='Unpaid')

    def __str__(self):
        return self.order_id


class Sale(models.Model):
    order_id = models.CharField(max_length=80)
    customer = models.CharField(max_length=150)
    product = models.CharField(max_length=120)
    quantity = models.PositiveIntegerField()
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateField()
    status = models.CharField(max_length=80, default='Completed')

    def __str__(self):
        return self.order_id


class Dispatch(models.Model):
    order_id = models.CharField(max_length=80)
    destination = models.CharField(max_length=200)
    carrier = models.CharField(max_length=150)
    date = models.DateField()
    status = models.CharField(max_length=80, default='In Transit')
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.order_id
