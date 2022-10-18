from .models import CarCategory, Category, Products
from rest_framework import serializers


class NameSerializer(serializers.Serializer):

    id = serializers.IntegerField()
    name = serializers.CharField()


class CarCategorySerializer(NameSerializer):
    pass


class CategorySerializer(NameSerializer):
    pass


class ProductSerializer(serializers.Serializer):

    id = serializers.IntegerField()
    name = serializers.CharField()
    year = serializers.IntegerField()
    brand = serializers.CharField()
    price = serializers.CharField()
    characteristics = serializers.CharField()
