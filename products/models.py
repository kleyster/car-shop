from django.db import models
from django.contrib.postgres.fields import JSONField, ArrayField
from _auth.models import Company


class CarCategory(models.Model):
    name = models.CharField(max_length=100)
    name_cn = models.CharField(max_length=150, default="")
    name_en = models.CharField(max_length=150, default="")
    image = models.ImageField()

    def __str__(self):
        return self.name

class CarType(models.Model):
    name = models.CharField(max_length=100)
    name_cn = models.CharField(max_length=150, default="")
    name_en = models.CharField(max_length=150, default="")
    car_category = models.ForeignKey(CarCategory, related_name="car_types", on_delete=models.CASCADE)
    image = models.ImageField()

    def __str__(self):
        return self.name


class Category(models.Model):

    name = models.CharField(max_length=150)
    name_cn = models.CharField(max_length=150, default="")
    name_en = models.CharField(max_length=150, default="")
    car_type = models.ManyToManyField(CarCategory, related_name="categories")

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.TextField()
    car_type = models.ForeignKey(CarType, related_name="products", on_delete=models.CASCADE)
    car_category = models.ForeignKey(CarCategory, related_name="product", on_delete=models.CASCADE, null=True)
    brand = models.ForeignKey(Company, related_name='products', on_delete=models.CASCADE)
    year = models.SmallIntegerField()
    price = models.IntegerField()
    model = models.CharField(max_length=100)
    car_brand = models.CharField(max_length=100)
    condition = models.CharField(max_length=100)
    engine = models.CharField(max_length=100)
    characteristics = ArrayField(models.JSONField())
    category = models.ForeignKey(Category, related_name="products", on_delete=models.SET_NULL, null=True)
    can_order = models.BooleanField(default=False)
    product_code = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.car_category = self.car_type.car_category
        super(Products, self).save(*args, **kwargs)


class ProductImages(models.Model):

    image = models.ImageField()
    product = models.ForeignKey(Products, related_name="images", on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name

