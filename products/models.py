from django.db import models


class CarCategory(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField()


class CarType(models.Model):
    name = models.CharField(100)
    car_category = models.ForeignKey(CarCategory, related_name="car_types", on_delete=models.CASCADE)
    image = models.ImageField()


class Category(models.Model):

    name = models.CharField(max_length=150)
    car_type = models.ManyToManyField(CarType, related_name="categories")


class Products(models.Model):
    name = models.TextField()
    car_type = models.ForeignKey(CarType, related_name="car_types", on_delete=models.CASCADE, null=True)
    brand = models.CharField(max_length=100)
    year = models.SmallIntegerField()
    price = models.IntegerField()
    characteristics = models.CharField(max_length=100)
    category = models.ForeignKey(Category, related_name="products", on_delete=models.SET_NULL, null=True)
    can_order = models.BooleanField(default=False)
    product_code = models.CharField(max_length=20)


class ProductImages(models.Model):

    image = models.ImageField()
    product = models.ForeignKey(Products, related_name="images", on_delete=models.CASCADE)
