from django.urls import path
from . import views


urlpatterns = [
    path("product_detail/<slug:slug>", views.product_detail, name="product"),
]
