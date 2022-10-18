from rest_framework import serializers
from .models import Cart
from products.models import Products, ProductImages
from products.serializers import ProductSerializer


class CartSerializer(serializers.Serializer):

    product = ProductSerializer()
    amount = serializers.IntegerField()