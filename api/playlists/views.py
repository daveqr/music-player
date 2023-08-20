from django.http import JsonResponse
from .models import Playlist, Track
from .serializers import PlaylistSerializer

def get_playlists(request):
    song1 = Track.objects.create(title="Smooth Operator", artist="Sade")
    song2 = Track.objects.create(title="Fuel", artist="Metallica")
    song3 = Track.objects.create(title="Iron Man", artist="Black Sabbath")
    song4 = Track.objects.create(title="Voodo Chile", artist="Jimi Hendrix")
    song5 = Track.objects.create(title="Pride and Joy", artist="Stevie Ray Vaughan")

    nightPl = Playlist.objects.create(name="Nighttime", description="Music to sleep to")
    workoutPl = Playlist.objects.create(name="Workout", description="Take this playlist to the gym")
    bluesPl = Playlist.objects.create(name="Blues", description="Best of the blues")

    nightPl.tracks.add(song1, song4)
    workoutPl.tracks.add(song2, song3)
    bluesPl.tracks.add(song4, song5)

    playlists = [nightPl, workoutPl, bluesPl]
    serializer = PlaylistSerializer(playlists, many=True)

    return JsonResponse(serializer.data, safe=False)
