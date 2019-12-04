from django.db import models
from datetime import datetime as dt
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=200, default='Nothing', null=True)
    product_type = models.CharField(max_length=200, default='Nothing', null=True)
    size = models.CharField(max_length=200, default='Nothing', null=True)
    color = models.CharField(max_length=200, default='Nothing', null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=100, null=True)
    description = models.TextField(blank=True, default='Nothing', null=True)
    address = models.TextField(blank=True, default='Nothing', null=True)
    is_available = models.BooleanField(default=True)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.title} - {self.price}"


class Order(models.Model):
    date_time = models.DateTimeField(default=dt.now)
    shop_pk = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{shop_pk}: {self.pk}'


class Selling(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
