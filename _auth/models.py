from django.db import models
from django.contrib.auth.models import AbstractBaseUser, User


class Users(AbstractBaseUser):

    id = models.UUIDField(primary_key=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=60, null=True)
    last_name = models.CharField(max_length=60, null=True)
    image = models.ImageField(upload_to="user/icons/", null=True)
    address = models.TextField(null=True)

    REQUIRED_FIELDS = ['email']