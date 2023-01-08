from rest_framework.generics import GenericAPIView, ListAPIView
from .serializers import *
from .models import *
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class CarCategoryView(ListAPIView):

    queryset = CarCategory.objects.all()
    serializer_class = CarCategorySerializer


class ProductsListView(ListAPIView):

    queryset = Products.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, pk):
        query = {}
        if request.query_params.get('category'):
            query['category'] = request.query_params['category']
        if request.query_params.get('car_type'):
            query['car_type'] = request.query_params['car_type']
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
        serializer = self.serializer_class(queryset, many=True)
        options = {
            "brands": queryset.distinct("brand"),
            "max_year": queryset.order_by("year").distinct("brand")[0],
            "max_price": queryset.order_by("price").distinct("price")[0],
            "min_price": queryset.order_by("-price").distinct("price")[0],
            "min_year": queryset.order_by("-year").distinct("brand")[0],
            "car_type": queryset.distinct("car_type")
        }
        return Response(serializer.data)


class AdminProductCreateView(GenericAPIView):

    serializer_class = ProductSerializer
    queryset = Products.objects.all()

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def get(self, request):
        company = request.user.company
        queryset = self.queryset.filter(brand_id=company.id)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializers.data)

class AdminProductView(GenericAPIView):

    serializer_class = ProductSerializer
    queryset = Products.objects.all()

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