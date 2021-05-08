from rest_framework import serializers

from product import models as m


class ProductModelSerializer(serializers.ModelSerializer):
    price = serializers.DecimalField(
        max_digits=9, decimal_places=2, coerce_to_string=False
    )

    class Meta:
        model = m.Product
        fields = [
            "id",
            "name",
            "price",
            "units_available",
            "on_sale",
            "product_variation",
            "created_at",
        ]
