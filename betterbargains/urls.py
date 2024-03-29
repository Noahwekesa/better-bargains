from django.contrib import admin

from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", include("pages.urls")),
    path("", include("product.urls")),
    # all auth
    path("accounts/", include("allauth.urls")),
    path("cart/", include("cart.urls")),
    path("admin/", admin.site.urls),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
