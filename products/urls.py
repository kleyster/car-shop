from django.urls import path
from .views import *

urlpatterns = [
    path("car-types/", CarCategoryView.as_view()),
    path("car-types/<int:pk>", CategoryView.as_view()),
    path("categories/<int:pk>", ProductsListView.as_view()),
    path("products/<int:pk>", ProductRetrieveView.as_view()),
]