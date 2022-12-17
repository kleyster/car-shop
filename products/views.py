from rest_framework.generics import GenericAPIView, ListAPIView
from .serializers import *
from .models import *
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class CategoryView(ListAPIView):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request, pk):
        queryset = self.get_queryset().filter(car_type=pk)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class CarCategoryView(ListAPIView):

    queryset = CarCategory.objects.all()
    serializer_class = CarCategorySerializer


class CarTypeView(ListAPIView):

    queryset = CarType.objects.all()
    serializer_class = NameSerializer

    def get(self, request, pk):
        queryset = self.get_queryset().filter(car_category=pk)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


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
