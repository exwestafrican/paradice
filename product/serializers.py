from rest_framework import serializers

from product import models as m


class ProductModelSerializer(serializers.Serializer):
    class Meta:
        model = m.Product
        fields = [
            "id",
            "name",
            "price",
            "units_available",
            "on_sale",
            "product_variation",
        ]
