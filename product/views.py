from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from product import serializers as ps
from product.models import Product


class ProductModelViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ps.ProductModelSerializer
