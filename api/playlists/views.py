from rest_framework import generics
from .models import Playlist
from .serializers import PlaylistSerializer
from django.http import JsonResponse

class PlaylistListCreateView(generics.ListCreateAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer

class PlaylistDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer

def get_playlists(request):
    # Create an empty list
    playlists = []

    # Return the empty list as JSON response
    return JsonResponse(playlists, safe=False)