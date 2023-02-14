import random
from django.core.cache import cache
from django.conf import settings
from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken


def generate_random_int(length=5):
    min_range = 10**(length-1)
    max_range = int("".join('9' for i in range(length)))
    return random.randint(min_range, max_range)


def send_verification_to_email(email: str):
    code = str(generate_random_int())
    cache.set(email, code, timeout=int(settings.CACHE_TTL))
    dd = send_mail(subject = "VERIFICATION CODE TO CAR SHOP", message=code, from_email=settings.EMAIL_HOST_USER, recipient_list=[email])


def check_verification_code(instance, code: str):
    if cache.get(instance.email) != str(code):
        return Response(status=status.HTTP_400_BAD_REQUEST)
    cache.delete(instance.email)
    token = RefreshToken.for_user(instance)
    return Response({
            "refresh": str(token),
            "access": str(token.access_token)
        })
