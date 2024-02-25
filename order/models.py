from django.db import models
from django.conf import settings

# from django.contrib.auth.models import User

from product.models import Product


class Order(models.Model):

    ORDERED = "ordered"
    SHIPPED = "shipped"

    STATUS_CHOICES = ((ORDERED, "ordered"), (SHIPPED, "shipped"))

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE
    )
    # user = models.ForeignKey(
    #     User, related_name="orders", blank=True, null=True, on_delete=models.CASCADE
    # )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.PositiveIntegerField()
    location = models.CharField(max_length=255)
    place = models.CharField(max_length=255)
    created_at = models.DateTimeField(
        auto_now_add=True
    )  # check when the order was created

    paid = models.BooleanField(default=False)  # check the status of the order
    paid_amount = models.IntegerField(blank=True, null=True)  # Amount to be paid

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=ORDERED)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name="items", on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField(default=1)
