from django.db import models
from user.models import *
# Create your models here.
Restaurant_category = (
    (1, 'Fast Food'),
    (2, 'Dessert'),
    (3, 'Chinese'),
    (4, 'Thai'),
    (5, 'Indian'),
    (6, 'Pakistani'),
    (7, 'Continental')
)
class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length = 50)
    avg_rating = models.FloatField(default=0)
    category = models.PositiveSmallIntegerField(choices = Restaurant_category)
    
    def __str__(self):
        return f"{self.name}, {self.address}, {self.avg_rating}, {self.category}"

class Rate(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    rate = models.PositiveSmallIntegerField()

    def __str(self):
        return f"{self.rate}"

class Seller(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    phone_number = models.PositiveSmallIntegerField()
    restaurant = models.OneToOneField(Restaurant, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.user}, {self.restaurant}, {self.phone_number}"

class Dish(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    summary = models.CharField(max_length=250)
    nationality = models.CharField(max_length=64)
    no_of_serving = models.PositiveSmallIntegerField()
    picture = models.CharField(max_length=64)
    category = models.CharField(max_length=64)
    glutten_free = models.BooleanField(default=False)
    customizable = models.BooleanField(default=False)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name="cooks")
    price = models.FloatField()

    def __str__(self):
        return f"{self.restaurant}, {self.seller}'s ,{self.name}, {self.summary}, {self.nationality}, {self.no_of_serving}, {self.picture}, {self.category}, {self.glutten_free}, {self.customizable}, {self.price} "

class Ingredient(models.Model):
    name = models.CharField(max_length=64)
    calorie_count  = models.FloatField()
    price = models.FloatField()
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name="dishingredient")

    def __str__(self):
        return f"{self.name}"

