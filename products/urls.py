from django.urls import path
from .views import *

urlpatterns = [
    path("car-categories/", CarCategoryView.as_view()),
    # path("car-types/<int:pk>", CarTypeView.as_view()),
    # path("categories/<int:pk>", CategoryView.as_view()),
    path("admin/products/", AdminProductCreateView.as_view()),
    path("admin/products/<int:pk>/images", ProductsImagesView.as_view()),
    path("admin/products/image/<int:pk>", ProductImageView.as_view()),
    path("products/<int:pk>", ProductsListView.as_view()),
    path("product/<int:pk>", ProductRetrieveView.as_view()),
    path("admin/product/<int:pk>", AdminProductView.as_view()),
    path('admin/car-categories/', CarCategorySuperAdminView.as_view()),
    path("products/options/<int:pk>", ProductFilterOptions.as_view()),
]
