from rest_framework import serializers
from _auth.models import Company


class EmailValidator(serializers.Serializer):

    email = serializers.EmailField()


class UserSerializer(serializers.Serializer):

    email = serializers.EmailField()
    first_name = serializers.CharField(allow_null=True)
    last_name = serializers.CharField(allow_null=True)
    address = serializers.CharField(allow_null=True)
    image = serializers.ImageField(allow_null=True)
    password = serializers.CharField(write_only=True)


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ("id", "name", "logo", "certificate", "description")

