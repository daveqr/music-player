from django.http import JsonResponse
from .models import Playlist, Track
from .serializers import PlaylistSerializer


def get_playlists(request):
    track1 = Track.objects.create(
        artist="Elvis", title="Never Been to Spain", url="http://localhost:8000/mp3/Elvis.mp3")
    track2 = Track.objects.create(
        artist="MTTV", title="Shane", url="http://localhost:8000/mp3/Shane.mp3")
    track3 = Track.objects.create(
        artist="Paul Shortino", title="Love of My Life", url="http://localhost:8000/mp3/Shortino.mp3")
    track4 = Track.objects.create(
        artist="James Whild Lea", title="Big Family", url="http://localhost:8000/mp3/Big Family.mp3")
    track5 = Track.objects.create(
        artist="James Whild Lea", title="The Smile Of Elvis", url="http://localhost:8000/mp3/The Smile Of Elvis.mp3")

    singerPl = Playlist.objects.create(
        name="Singers", description="Tracks from popular signers")
    therapyPl = Playlist.objects.create(
        name="Therapy", description="Tracks from the album Therapy")
    rockPl = Playlist.objects.create(name="Rock", description="Best of rock")

    singerPl.tracks.add(track1, track3)
    therapyPl.tracks.add(track4, track5)
    rockPl.tracks.add(track2, track1)

    playlists = [singerPl, therapyPl, rockPl]
    serializer = PlaylistSerializer(playlists, many=True)

    return JsonResponse(serializer.data, safe=False)
