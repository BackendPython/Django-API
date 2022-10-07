from .serializer import *
from rest_framework import permissions
from django.shortcuts import render
from rest_framework.response import Response
from .models import Product
from rest_framework.decorators import api_view, permission_classes


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def home(request):
    product = Product.objects.all()
    serializer = ProductApi(product, many=True)
    return Response(serializer.data)

