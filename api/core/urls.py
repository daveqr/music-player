from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),

    path('playlists/', include('playlists.urls')),
    path('upload/', include('uploads.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
