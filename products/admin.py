from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Products)
admin.site.register(Category)
admin.site.register(CarCategory)
admin.site.register(ProductImages)
admin.site.register(CarType)

