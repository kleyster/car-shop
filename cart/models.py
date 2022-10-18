from django.db import models
from products.models import Products
from django.contrib.auth.models import User


class Cart(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cart")
    amount = models.IntegerField(default=1)


class Favourites(models.Model):

    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="favourites")
