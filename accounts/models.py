from django.db import models

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=254, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    INDOOR = 'indoor'
    OUTDOOR = 'outdoor'

    CATEGORY = [
        (INDOOR, 'Indoor'),
        (OUTDOOR, 'Outdoor')
    ]

    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    tags = models.ManyToManyField(Tag)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    PENDING = 'Pending'
    OUT_FOR_DELIVERY = 'OFD'
    DELIVERED = 'Delivered'

    STATUS = [
        (PENDING, 'Pending'),
        (OUT_FOR_DELIVERY, 'Out For Delivery'),
        (DELIVERED, 'Delivered')
    ]

    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)

    def __str__(self):
        return self.product
