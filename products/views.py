from rest_framework.generics import GenericAPIView, ListAPIView
from .serializers import *
from .models import *
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from drf_yasg.utils import swagger_auto_schema
from products.swagger_utils import CAR_TYPE_QUERY, CATEGORY_QUERY, PRODUCT_SEARCH
from _auth.models import Company
from django.db.models import Q


class CarCategoryView(ListAPIView):

    queryset = CarCategory.objects.all()
    serializer_class = CarCategorySerializer


class ProductsImagesView(GenericAPIView):

    queryset = ProductImages.objects.all()
    serializer_class = ProductImageSerializer
    permissions = [IsAdminUser,]
    
    def get(self, request, pk):
        images = self.queryset.filter(product_id=pk)
        serializer = self.serializer_class(images, many=True)
        return Response(serializer.data)

    def post (self, request, pk):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        image = ProductImages.objects.create(**serializer.validated_data)
        return Response(self.serializer_class(image))


class ProductImageView(GenericAPIView):
    permissions = [IsAdminUser, ]

    def delete(self, request, pk):
        Products.images.filter(pk=pk).delete()
        return Response()


class ProductsListView(ListAPIView):

    queryset = Products.objects.all()
    serializer_class = ProductSerializer

    @swagger_auto_schema(manual_parameters=[CAR_TYPE_QUERY, CATEGORY_QUERY, PRODUCT_SEARCH])
    def get(self, request, pk):
        query = {}
        if request.query_params.get('search'):
            query['name__icontains'] = request.query_params['search']
        if request.query_params.get('category'):
            query['category__in'] = request.query_params.getlist('category')
        if request.query_params.get('car_type'):
            query['car_type__in'] = request.query_params.getlist('car_type')
        if request.query_params.getlist('year'):
            query['year__in'] = request.query_params.getlist('year')
        if request.query_params.get('price_gte'):
            query['price__gte'] = request.query_params['price_gte']
        if request.query_params.get('price_lte'):
            query['price__lte'] = request.query_params['price_lte']
        queryset = self.get_queryset().filter(car_category=pk, **query)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class ProductRetrieveView(GenericAPIView):

    queryset = Products.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, pk):
        queryset = self.get_queryset().get(id=pk)
        serializer = self.serializer_class(queryset)
        return Response(serializer.data
                        )


class ProductFilterOptions(GenericAPIView):

    serializer_class = NameSerializer
    queryset = Products.objects.all()

    def get(self, request, pk):
        queryset = self.get_queryset().filter(car_category=pk)
        car_type = CarType.objects.filter(id__in=queryset.distinct("car_type_id").values_list("car_type_id", flat=True))
        brands = Company.objects.filter(id__in=queryset.distinct("brand_id").values_list('brand', flat=True))
        options = {
            "brands": self.serializer_class(brands, many=True).data,
            "max_year": queryset.order_by("year").distinct('year').values_list('year', flat=True),
            "max_price": queryset.order_by("price").first().price if queryset.exists() else None,
            "min_price": queryset.order_by("-price").first().price if queryset.exists() else None,
            "car_type": self.serializer_class(car_type, many=True).data
        }
        return Response(options)


class AdminProductCreateView(GenericAPIView):

    serializer_class = ProductSerializer
    queryset = Products.objects.all()
    permissions = [IsAdminUser,]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(brand_id=request.user.company.id)
        return Response(serializer.data)
    
    def get(self, request):
        company = request.user.company
        queryset = self.queryset.filter(brand_id=company.id)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class AdminProductView(GenericAPIView):

    serializer_class = ProductSerializer
    queryset = Products.objects.all()
    permissions = [IsAdminUser,]

    def get(self,request, pk):
        queryset = self.queryset.get(pk=pk)
        serializer = self.serializer_class(queryset)
        return Response(serializer.data)

    def put(self, request, pk):
        instance = self.queryset.get(pk=pk)
        serializer = self.serializer_class(instance=instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self,request,pk):
        instance = get_object_or_404(self.queryset, pk=pk)
        instance.delete()
        return Response()


class CarCategorySuperAdminView(GenericAPIView):

    serializer_class = CarCategoryAdminSerializer
    queryset = CarCategory.objects.all()
    permissions = [IsAdminUser, ]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class ProductSearchView(GenericAPIView):

    serializer_class = NameSerializer
    queryset = Products.objects.all()

    @swagger_auto_schema(manual_parameters=[PRODUCT_SEARCH])
    def get(self, request):
        search_text = request.query_params.get('search')
        if search_text is None:
            return Response(status=404)
        queryset = self.queryset.filter(name__icontains=search_text)
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)