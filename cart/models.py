from django.db import models
from products.models import Products
from _auth.models import Users

class Cart(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name="cart")
    amount = models.IntegerField(default=1)


class Favourites(models.Model):

    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name="favourites")
