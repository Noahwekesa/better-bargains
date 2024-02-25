from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("faq/", views.faq_view, name="faq"),
    path("about/", views.about_view, name="about"),
    path("shop/", views.shop, name="shop"),
]
