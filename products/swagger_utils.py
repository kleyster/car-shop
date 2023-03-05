from drf_yasg import openapi

CAR_TYPE_QUERY = openapi.Parameter('car_type', openapi.IN_QUERY, type=openapi.TYPE_INTEGER)
CATEGORY_QUERY = openapi.Parameter('category', openapi.IN_QUERY, type=openapi.TYPE_INTEGER)
PRODUCT_SEARCH = openapi.Parameter('search', openapi.IN_QUERY, type=openapi.TYPE_STRING)

