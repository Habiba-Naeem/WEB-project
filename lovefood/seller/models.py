from django.db import models
from django.db import models
from user.models import Seller

# Create your models here.

# Create your models here.
class Dish(models.Model):
    name = models.CharField(max_length=64)
    summary = models.CharField(max_length=250)
    nationality = models.CharField(max_length=64)
    no_of_serving =models.IntegerField()
    picture = models.CharField(max_length=64)
    category = models.CharField(max_length=64)
   # glutten_free = models.CharField(max_length=1)
   # customizable = models.CharField(max_length=1)
    glutten_free = models.BooleanField(default=False)
    customizable = models.BooleanField(default=False)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name="cooks", default='DEFAULT VALUE' )

    def __str__(self):
        return f"{self.seller.name}'s {self.name}"

class Ingredient(models.Model):
    name = models.CharField(max_length=64)
    calorie_count  = models.FloatField()
    price = models.FloatField()
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name="dishingredient")

    def __str__(self):
        return f"{self.name}"
