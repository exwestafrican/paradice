import uuid

from django.conf import settings
from django.db import models

from product.models import Product
from utils.mixins import TimeStampMixin

# Create your models here.


class OrderStatus(TimeStampMixin):
    name = models.CharField(max_length=200)
    description = models.TextField()

    @classmethod
    def get_default_pk(cls):
        status, created = cls.objects.get_or_create(
            name="pending",
            defaults={"description": "customer has attempted to pay for order"},
        )
        return status.pk


class Order(TimeStampMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="order_owner",
    )
    anon_customer = models.BooleanField(default=True)
    customer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="ordered_by",
    )
    delivery_address = models.TextField(help_text="where would you like this delivered")
    land_mark = models.TextField(
        help_text="where would you like this delivered", null=True, blank=True
    )
    instructions = models.TextField()
    delivery_fee = models.PositiveIntegerField(default=1000)
    tax = models.DecimalField(max_digits=9, decimal_places=2)
    status = models.ForeignKey(
        OrderStatus,
        related_name="order_status",
        default=OrderStatus.get_default_pk,
        on_delete=models.CASCADE,
    )
    payment_refrence = models.CharField(
        max_length=500, null=True, blank=True, help_text="payment gateway refrence"
    )

    # date_shipped,created_at , customer_ID ,payment_ID , status=["in_transit","delivered"] , tax

    # total = item.total - item.discount


class Item(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="item")
    # discount

    def __str__(self):
        return "{} {} of {}".format(
            self.quantity, self.product.measured_in.name, self.product
        )

    def total(self):
        return self.quantity * self.product.current_price
