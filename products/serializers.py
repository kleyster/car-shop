from rest_framework import serializers


class NameSerializer(serializers.Serializer):

    id = serializers.IntegerField()
    name = serializers.CharField()


class CarCategorySerializer(NameSerializer):
    pass


class CategorySerializer(NameSerializer):

    pass
    # car_type = serializers.CharField(source="car_type.name")
    # catalog = serializers.CharField(source="car_type.car_category.name")


class ProductSerializer(serializers.Serializer):

    id = serializers.IntegerField()
    name = serializers.CharField()
    year = serializers.IntegerField()
    brand = serializers.CharField()
    price = serializers.CharField()
    characteristics = serializers.CharField()
