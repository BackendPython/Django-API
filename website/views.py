from .serializer import *
from rest_framework import permissions
from django.shortcuts import render
from rest_framework.response import Response
from .models import Product
from rest_framework.decorators import api_view, permission_classes




# main API
@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def home(request):
    product = Product.objects.all()
    serializer = ProductApi(product, many=True)
    return Response(serializer.data)


# filter adidas
@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def filter_adidas(request):
    product = Product.objects.filter(brend='adidas')
    serializer = ProductApi(product, many=True)
    return Response(serializer.data)

# filter nike
@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def filter_nike(request):
    product = Product.objects.filter(brend='nike')
    serializer = ProductApi(product, many=True)
    return Response(serializer.data)

# API post joylash

@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def postPaste(request):
    serializer = ProductApi(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

