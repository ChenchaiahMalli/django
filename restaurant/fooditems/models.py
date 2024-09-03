from django.db import models


class FoodItems(models.Model):
    name = models.CharField(max_length=50)
    items= models.IntegerField()
    foodtype = models.CharField(max_length=100)
    price = models.IntegerField()
# Create your models here.
