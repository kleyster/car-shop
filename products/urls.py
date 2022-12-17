from django.urls import path
from .views import *

urlpatterns = [
    path("car-categories/", CarCategoryView.as_view()),
    path("car-types/<int:pk>", CarTypeView.as_view()),
    path("categories/<int:pk>", CategoryView.as_view()),
    path("products/<int:pk>", ProductsListView.as_view()),
    path("product/<int:pk>", ProductRetrieveView.as_view()),
    path("product/options/<int:pk>", ProductFilterOptions.as_view()),
]
