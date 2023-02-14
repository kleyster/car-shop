from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from .models import Users, Company
from .serializers import EmailValidator, UserSerializer, CompanySerializer
from .utils import send_verification_to_email, check_verification_code
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status


class AuthenticationView(GenericAPIView):

    serializer_class = EmailValidator

    def post(self, request):
        serializer = EmailValidator(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance, created = Users.objects.get_or_create(email=serializer.validated_data['email'])
        instance.save()
        send_verification_to_email(instance.email)
        return Response(status=status.HTTP_201_CREATED)


class AuthenticationVerificationView(GenericAPIView):

    serializer_class = EmailValidator

    def post(self, request):

        serializer = EmailValidator(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = get_object_or_404(Users, email=serializer.validated_data['email'])
        request_code = request.data.get('request_code')
        return check_verification_code(instance, request_code)


class UserView(GenericAPIView):

    serializer_class = UserSerializer

    def get(self, request):
        return Response(
            UserSerializer(request.user).data
        )

    def post(self, request):
        if not request.user.is_superuser:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            serializer.data
        )


class CompanyView(GenericAPIView):

    serializer_class = CompanySerializer

    def get(self, request):
        instance = request.user.company
        return Response(
            self.serializer_class(instance).data
        )

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(created_by=request.user)
        return Response(serializer.data)


class CompanyDetailView(GenericAPIView):

    serializer_class = CompanySerializer
    queryset = Company.objects.all()

    def get(self, request, pk):
        instance = get_object_or_404(self.queryset, pk=pk)
        return Response(
            self.serializer_class(instance).data
        )
