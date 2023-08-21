from django.http import JsonResponse
from .models import Playlist, Track
from .serializers import PlaylistSerializer
from django.conf import settings


def get_playlists(request):
    track1 = Track.objects.create(
        artist="StudioKolomna", title="Risk", url=f"{settings.BASE_URL}/StudioKolomna_risk.mp3")
    track2 = Track.objects.create(
        artist="Lexin Music", title="Inspiring Cinematic Ambient", url=f"{settings.BASE_URL}/lexin_inspiring-cinematic-ambient.mp3")
    track3 = Track.objects.create(
        artist="Universefield", title="Creepy Piano", url=f"{settings.BASE_URL}/UNIVERSFIELD_creepy-piano.mp3")
    track4 = Track.objects.create(
        artist="Keyfram Audio", title="Now This", url=f"{settings.BASE_URL}/now-this-Keyframe_Audio.mp3")
    track5 = Track.objects.create(
        artist="Fassounds", title="Good Night", url=f"{settings.BASE_URL}/fassounds_good-night.mp3")
    track56 = Track.objects.create(
        artist="Leva", title="Eternity", url=f"{settings.BASE_URL}/leva_eternity.mp3")

    cinematicPl = Playlist.objects.create(
        name="Cinematic", description="Cinematic tracks")
    mysteriousPl = Playlist.objects.create(
        name="Mysterious", description="Mysterious tracks")
    romanticPl = Playlist.objects.create(
        name="Romantic", description="Romantics tracks")

    cinematicPl.tracks.add(track1, track2)
    mysteriousPl.tracks.add(track3, track4)
    romanticPl.tracks.add(track5, track56)

    playlists = [cinematicPl, mysteriousPl, romanticPl]
    serializer = PlaylistSerializer(playlists, many=True)

    return JsonResponse(serializer.data, safe=False)
