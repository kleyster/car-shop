from .views import *
from django.urls import path

urlpatterns = [
    path("favourites/", FavouritesView.as_view()),
    path("favourites/<int:pk>", FavouritesAddView.as_view()),
    path("cart/", CartProductView.as_view()),
    path("cart/<int:pk>", CartProductAddView.as_view()),
]