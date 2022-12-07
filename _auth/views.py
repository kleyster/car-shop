from rest_framework.views import APIView
from .models import Users
from .serializers import EmailValidator, UserSerializer
from.utils import generate_random_int
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from django.core import cache
from core.settings import CACHE_TTL
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken


class AuthenticationView(APIView):

    def post(self, request):
        serializer = EmailValidator(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = Users.objects.get_or_create(email=serializer.email)
        instance.save()
        cache.set(instance.email, str(generate_random_int()), timeout=int(CACHE_TTL))
        return Response(status=status.HTTP_201_CREATED)


class AuthenticationVerificationView(APIView):

    def post(self, request):

        serializer = EmailValidator(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = get_object_or_404(Users, email=serializer.email)
        request_code = request.data.get('security_code')
        if str(request_code) != str(cache.get(instance.email)):
            return Response(status=status.HTTP_400_BAD_REQUEST)
        cache.delete(instance.email)
        token = RefreshToken.for_user(instance)
        return Response({
                "refresh": str(token),
                "access": str(token.access_token)
            })


class UserView(APIView):

    def get(self, request):
        return Response(
            UserSerializer(request.user)
        )
