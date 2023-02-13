from rest_framework import serializers
from .models import Products, ProductImages


class ProductImageSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
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

    images = ProductImageSerializer(many=True, read_only=True)
    images = serializers.ListField(write_only=True, child=serializers.ImageField())
    brand = serializers.IntegerField(read_only=True, source="brand.id")

    class Meta:
        model = Products
        fields = "__all__"


    def create(self, validated_data):
        images = validated_data.pop('images', [])
        instance = super().create(validated_data)
        for image in images:
            ProductImages.objects.create(image=image, product_id=instance.id)
        return instance


class CarCategoryAdminSerializer(NameSerializer, ProductImageSerializer):
    
    id = serializers.IntegerField(read_only=True)


    def create(self, validated_data, **kwargs):
        return CarCategory.objects.create(**validated_data)

