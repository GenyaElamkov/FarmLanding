from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("ecoadmin/", admin.site.urls),
    path("", include("lending.urls")),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [path('summernote/', include('django_summernote.urls'))]
else:
    urlpatterns += [path('summernote/', include('django_summernote.urls'))]