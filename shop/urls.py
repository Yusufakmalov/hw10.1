from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from shop2.views import base_page, about_page
from shop import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', base_page),
    path('about', about_page),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
