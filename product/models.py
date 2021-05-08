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
    product_code = models.CharField(default=Utils.generate_prd_code)

    def __str__(self):
        return self.name


class Image(TimeStampMixin):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    img_variation = models.JSONField(default=dict)

    def __str__(self):
        pass

    class Meta:
        db_table = ""
        managed = True
        verbose_name = "Image"
        verbose_name_plural = "Images"
