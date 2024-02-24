from django.db import models
from django.contrib.auth.models import User


class Order(models.Model):
    user = models.ForeignKey(
        User, related_name="orders", blank=True, null=True, on_delete=models.CASCADE
    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.PositiveIntegerField()
    location = models.CharField(max_length=255)
    place = models.CharField(max_lenght=255)
    created_at = models.DateTimeField(
        auto_now_add=True
    )  # check when the order was created

    paid = models.BooleanField(default=False)  # check the status of the order
    paid_amount = (models.IntegerField(blank=True, null=True),)  # Amount to be paid
