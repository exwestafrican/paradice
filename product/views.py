from django.shortcuts import render

# Create your views here.
from rest_framework import status, viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from product import serializers as ps
from product.models import Product


class ProductModelViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.first()
    serializer_class = ps.ProductModelSerializer

    def list(self, request):
        queryset = self.get_queryset()
        print(queryset)
        serializer = self.serializer_class(queryset)
        print(serializer)
        return Response(
            {"success": True, "message": "success", "data": serializer.data},
            status=status.HTTP_200_OK,
        )
