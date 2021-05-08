from rest_framework import serializers

from product import models as m


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.Image
        fields = ["img_variation"]


class ProductModelSerializer(serializers.ModelSerializer):
    product_image = ImageSerializer(many=True)
    price = serializers.DecimalField(
        max_digits=9, decimal_places=2, coerce_to_string=False
    )

    class Meta:
        model = m.Product
        fields = [
            "id",
            "product_image",
            "name",
            "price",
            "units_available",
            "on_sale",
            "product_code",
            "product_variation",
            "created_at",
        ]
