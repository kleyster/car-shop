from rest_framework import serializers


class EmailValidator(serializers.Serializer):

    email = serializers.EmailField()


class UserSerializer(serializers.Serializer):

    email = serializers.EmailField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    address = serializers.CharField()
    image = serializers.ImageField()
