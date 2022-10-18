from django.db import models


class CarCategory(models.Model):
    name = models.CharField(max_length=100)


class Category(models.Model):

    name = models.CharField(max_length=150)
    car_category = models.ForeignKey(CarCategory, on_delete=models.SET_NULL, related_name="categories", null=True)


class Products(models.Model):
    name = models.TextField()
    brand = models.CharField(max_length=100)
    year = models.SmallIntegerField()
    price = models.IntegerField()
    characteristics = models.CharField(max_length=100)
    category = models.ForeignKey(Category, related_name="products", on_delete=models.SET_NULL, null=True)


class ProductImages(models.Model):

    image = models.ImageField()
    product = models.ForeignKey(Products, related_name="images", on_delete=models.CASCADE)
