from rest_framework.generics import GenericAPIView, ListAPIView
from .serializers import *
from .models import *
from rest_framework.response import Response


class CategoryView(ListAPIView):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request, pk):
        queryset = self.get_queryset().filter(car_category=pk)
        serializer = self.serializer_class(queryset,many=True)
        return Response(serializer.data)

class CarCategoryView(ListAPIView):

    queryset = CarCategory.objects.all()
    serializer_class = CarCategorySerializer


class ProductsListView(ListAPIView):

    queryset = Products.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, pk):
        queryset = self.get_queryset().filter(category=pk)
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
