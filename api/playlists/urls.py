from django.urls import path
from .views import PlaylistView

urlpatterns = [
    path('', PlaylistView.as_view({'get': 'retrieve'}))
]
