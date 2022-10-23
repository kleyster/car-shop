from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):


    class Meta:
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password']
        model = User

    extra_kwargs = {
        "id": {"read_only": True},
    }

    def validate_password(self, attrs):
        attrs['password'] = make_password(attrs.get('password'))
        return attrs