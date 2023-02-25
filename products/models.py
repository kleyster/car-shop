from django.db import models
from django.contrib.postgres.fields import JSONField, ArrayField
from _auth.models import Company


class CarCategory(models.Model):
    name = models.CharField(max_length=100)
    name_cn = models.CharField(max_length=150)
    image = models.ImageField()


class CarType(models.Model):
    name = models.CharField(max_length=100)
    name_cn = models.CharField(max_length=150)
    car_category = models.ForeignKey(CarCategory, related_name="car_types", on_delete=models.CASCADE)
    image = models.ImageField()


class Category(models.Model):

    name = models.CharField(max_length=150)
    name_cn = models.CharField(max_length=150)
    car_type = models.ManyToManyField(CarCategory, related_name="categories")


class Products(models.Model):
    name = models.TextField()
    car_type = models.ForeignKey(CarType, related_name="products", on_delete=models.CASCADE)
    car_category = models.ForeignKey(CarCategory, related_name="product", on_delete=models.CASCADE, null=True)
    brand = models.ForeignKey(Company, related_name='products', on_delete=models.CASCADE)
    year = models.SmallIntegerField()
    price = models.IntegerField()
    characteristics = ArrayField(models.JSONField())
    category = models.ForeignKey(Category, related_name="products", on_delete=models.SET_NULL, null=True)
    can_order = models.BooleanField(default=False)
    product_code = models.CharField(max_length=20)

    def save(self, *args, **kwargs):
        self.car_category = self.car_type.car_category
        super(Products, self).save(*args, **kwargs)


class ProductImages(models.Model):

    image = models.ImageField()
    product = models.ForeignKey(Products, related_name="images", on_delete=models.CASCADE)
