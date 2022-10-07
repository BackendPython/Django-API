from dataclasses import fields
from rest_framework import serializers
from .models import *

class ProductApi(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['title', 'brend', 'price']



