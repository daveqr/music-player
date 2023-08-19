from django.urls import path
from .views import get_playlists

urlpatterns = [
    path('', get_playlists, name='get-playlists'),
]