from django.db import models

class Product(models.Model):
    
    brend = models.CharField(max_length=20)
    title = models.CharField(max_length=20)
    price = models.IntegerField(default=100)
    
