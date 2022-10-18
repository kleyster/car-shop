from rest_framework.views import APIView
from products.serializers import ProductSerializer
from rest_framework.response import Response
from products.models import Products
from .models import Favourites, Cart
from django.db.models import F
from .serializers import CartSerializer


class FavouritesView(APIView):

    serializer_class = ProductSerializer

    def get(self, request):
        user = Products.objects.filter(id__in=request.user.favourites.select_related("product").all().values_list("product",flat=True))
        serializer = ProductSerializer(user, many=True)
        return Response(serializer.data)


class FavouritesAddView(APIView):

    def put(self, request, pk):
        product, created = Favourites.objects.get_or_create(user=request.user, product_id=pk)
        return Response()

class CartProductView(APIView):

    serializers_class = CartSerializer

    def get(self, request):
        products = Cart.objects.filter(user=request.user)
        serializer = self.serializers_class(products, many=True)
        return Response(serializer.data)


class CartProductAddView(APIView):

    def put(self,request, pk):
        product, created = Cart.objects.get_or_create(user=request.user, product_id=pk)
        print(created)
        if not created:
            product.amount += F("amount")
            product.save()
        return Response()
