from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("authentication.urls")),
    path("api/v1/", include("customers.urls")),
    path("api/v1/", include("parking.urls")),
    path("api/v1/", include("vehicles.urls")),
]


urlpatterns += static(settings.STATIC_URL, docuemnt_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, docuemnt_root=settings.MEDIA_ROOT)
