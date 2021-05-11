import uuid

from django.db import models

from utils.func import Utils
from utils.mixins import TimeStampMixin

# Create your models here.


class Product(TimeStampMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    units_available = models.PositiveSmallIntegerField()
    on_sale = models.BooleanField(default=False)
    product_variation = models.JSONField(default=dict)
    product_code = models.CharField(default=Utils.generate_prd_code, max_length=4)
    discount = models.DecimalField(max_digits=4, decimal_places=4)

    def __str__(self):
        return self.name

    @property
    def discount_price(self):
        return self.price * self.discount

    @property
    def current_price(self):
        price = self.price if on_sale is False else self.discount_price
        return price


class Image(TimeStampMixin):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="product_image"
    )
    img_variation = models.JSONField(default=dict)

    def __str__(self):
        return self.product.name

    class Meta:
        db_table = ""
        managed = True
        verbose_name = "Image"
        verbose_name_plural = "Images"
