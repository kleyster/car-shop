from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from orders.serializers import ApplicationFormSerializer
from django.shortcuts import get_object_or_404
from products.models import Products
from rest_framework.permissions import AllowAny, IsAdminUser
from _auth.models import Company
from core.utils import send_appilcation_mail


class ApplicationFormView(GenericAPIView):

    serializer_class = ApplicationFormSerializer
    permission_classes = [AllowAny,]

    def post(self, request, pk):
        instance = get_object_or_404(Products.objects.select_related('brand').all(), pk=pk)
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        application = serializer.save(product_id=instance.id, company_id=instance.brand_id)
        send_appilcation_mail(application, instance.brand.created_by.email)
        return Response(serializer.data)


class AdminApplicationFormView(GenericAPIView):

    serializer_class = ApplicationFormSerializer
    permission_classes = [IsAdminUser]

    def get(self, request):
        instance = get_object_or_404(
            Company.objects.prefetch_related('applications').all(), created_by_id=request.user.id
        )
        serializer = ApplicationFormSerializer(instance.applications, many=True)
        return Response(serializer.data)
