from django.http import JsonResponse
from .models import Playlist, Track
from .serializers import PlaylistSerializer


def get_playlists(request):
    track1 = Track.objects.create(
        artist="StudioKolomna", title="Risk", url="http://localhost:8000/mp3/StudioKolomna_risk.mp3")
    track2 = Track.objects.create(
        artist="Lexin Music", title="Inspiring Cinematic Ambient", url="http://localhost:8000/mp3/lexin_inspiring-cinematic-ambient.mp3")
    track3 = Track.objects.create(
        artist="Universefield", title="Creepy Piano", url="http://localhost:8000/mp3/UNIVERSFIELD_creepy-piano.mp3")
    track4 = Track.objects.create(
        artist="Keyfram Audio", title="Now This", url="http://localhost:8000/mp3/now-this-Keyframe_Audio.mp3")
    track5 = Track.objects.create(
        artist="Fasssounds", title="Good Night", url="http://localhost:8000/mp3/fassoumds_good-night.mp3")
    track56= Track.objects.create(
        artist="Leva", title="Eternity", url="http://localhost:8000/mp3/leva_eternity.mp3")

    cinematicPl = Playlist.objects.create(
        name="Cinematic", description="Cinematic tracks")
    mysteriousPl = Playlist.objects.create(
        name="Therapy", description="Mysterious tracks")
    romanticPl = Playlist.objects.create(name="Rock", description="Romantics tracks")

    cinematicPl.tracks.add(track1, track2)
    mysteriousPl.tracks.add(track3, track4)
    romanticPl.tracks.add(track5, track56)

    playlists = [cinematicPl, mysteriousPl, romanticPl]
    serializer = PlaylistSerializer(playlists, many=True)

    return JsonResponse(serializer.data, safe=False)
