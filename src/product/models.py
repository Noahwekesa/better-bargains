from django.db import models
from django.core.files import File
from product.consts import CATEGORY
from io import BytesIO
from PIL import Image


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
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

    def get_display_price(self):
        return self.price

    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return self.thumbnail.url
            else:
                return 'https://via.placeholder.com/240x240x.jpg'

    def make_thumbnail(self, image, size=(300, 300)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail
