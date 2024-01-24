from django.db import models

from product.consts import CATEGORY


class Category(models.Model):
    name = models.CharField(max_length=24, choices=CATEGORY)
    slug = models.SlugField()

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    category = models.ForeignKey(
        Category,
        related_name='products',
        on_delete=models.CASCADE)
    name = models.CharField(max_length=24)
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True)
    price = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'

    def get_display_price(self):
        return self.price
