from .views import *
from django.urls import path

urlpatterns = [
    path('', home),
    path('product-<int:pk>', singleapi, name='single-api'),
    path('adidas/', filter_adidas, name='filter-adidas'),
    path('<int:pk>-edit', postEdit, name='post-edit'),
    path('nike/', filter_nike, name='filter-nike'),
    path('add/', postPaste, name='product-add'),
]