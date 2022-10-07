from .views import *
from django.urls import path

urlpatterns = [
    path('', home),
    path('adidas/', filter_adidas, name='filter-adidas'),
    path('nike/', filter_nike, name='filter-nike')
    
]