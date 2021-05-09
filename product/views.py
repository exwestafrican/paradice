from django.shortcuts import render

# Create your views here.
from rest_framework import status, viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from product import serializers as ps
from product.models import Product


class ProductModelViewSet(viewsets.ModelViewSet):
    serializer_class = ps.ProductModelSerializer

    def get_queryset(self):
        return Product.objects.all()

    def list(self, request):
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
        serializer = self.serializer_class(page, many=True)
        return Response(
            self.get_paginated_response(
                {"success": True, "message": "success", "data": serializer.data}
            ),
            status=status.HTTP_200_OK,
        )
