from rest_framework import serializers
from .models import Products


class ProductImageSerializer(serializers.Serializer):

    id = serializers.IntegerField()
    image = serializers.ImageField()

class NameSerializer(serializers.Serializer):

    id = serializers.IntegerField()
    name = serializers.CharField()


class CarTypesSerializer(NameSerializer):

    image = serializers.ImageField()
    

class CategorySerializer(NameSerializer):

    pass
    # car_type = serializers.CharField(source="car_type.name")
    # catalog = serializers.CharField(source="car_type.car_category.name")


class CarCategorySerializer(NameSerializer):
    
    car_types = CarTypesSerializer(many=True)


class ProductSerializer(serializers.ModelSerializer):

    images = ProductImageSerializer(many=True)

    class Meta:
        model = Products
        fields = "__all__"