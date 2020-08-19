from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from seller.models import *
from deliverer.models import *
# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return f"{self.user}"

class Product(models.Model):
    dish = models.ForeignKey(Dish, on_delete = models.CASCADE)

    def __str__(self):
        return f"${self.dish}"

class Cart_Item(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default = 1)
    def __str__(self):
        return f"{self.product}, {self.cart},{self.quantity}"

class Order_Items(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE, null = True, blank = True)
    quantity = models.PositiveSmallIntegerField(default = 1)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null = True, blank = True)
    
    def __str__(self):
        return f"{self.product}, {self.quantity}, {self.cart}"

class Order(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    order_items = models.ForeignKey(Order_Items, on_delete=models.CASCADE)
    address = models.CharField(max_length = 100)
    phone_number = models.PositiveSmallIntegerField()
    total = models.DecimalField( max_digits = 20, decimal_places = 2 )
    deliverer = models.ForeignKey(Deliverer, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.order_items}, {self.total}"