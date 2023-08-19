from django.http import JsonResponse
from .models import Playlist, Song
from .serializers import PlaylistSerializer

def get_playlists(request):
    song1 = Song.objects.create(title="Smooth Operator", artist="Sade")
    song2 = Song.objects.create(title="Fuel", artist="Metallica")
    song3 = Song.objects.create(title="Iron Man", artist="Black Sabbath")
    song4 = Song.objects.create(title="Voodo Chile", artist="Jimi Hendrix")
    song5 = Song.objects.create(title="Pride and Joy", artist="Stevie Ray Vaughan")

    nightPl = Playlist.objects.create(name="Nighttime", description="Music to sleep to")
    workoutPl = Playlist.objects.create(name="Workout", description="Take this playlist to the gym")
    bluesPl = Playlist.objects.create(name="Blues", description="Best of the blues")

    nightPl.songs.add(song1, song4)
    workoutPl.songs.add(song2, song3)
    bluesPl.songs.add(song4, song5)

    playlists = [nightPl, workoutPl, bluesPl]
    serializer = PlaylistSerializer(playlists, many=True)

    return JsonResponse(serializer.data, safe=False)
