from django.http import JsonResponse
from django.views import View
from .models import Playlist, Track
from .serializers import PlaylistSerializer
from django.conf import settings
from rest_framework.viewsets import ViewSet


class PlaylistView(ViewSet):

    def retrieve(self, request):
        track1 = Track.objects.create(
            artist="Neon Octopus", title="Electric Tentacles", url=f"{settings.BASE_URL}/neon-octopus_electric-tentacles.mp3")
        track2 = Track.objects.create(
            artist="Frozen Fire", title="Melting Dreams", url=f"{settings.BASE_URL}/frozen-fire_melting-dreams.mp3")
        track3 = Track.objects.create(
            artist="Shadowplay Ensemble", title="Whispering Shadows", url=f"{settings.BASE_URL}/shadowplay-ensemble_whispering-shadows.mp3")
        track4 = Track.objects.create(
            artist="Astrofunk Odyssey", title="Alien Funk Encounter", url=f"{settings.BASE_URL}/astrofunk-odyssey_alien-funk-encounter.mp3")
        track5 = Track.objects.create(
            artist="Velvet Thunderstruck", title="Good Night", url=f"{settings.BASE_URL}/velvet-thunderstruck_good-night.mp3")
        track56 = Track.objects.create(
            artist="Galactic Groove Collective", title="Eternity", url=f"{settings.BASE_URL}/galactic-groove-collective_eternity.mp3")

        cinematicPl = Playlist.objects.create(
            name="Cinematic", description="Cinematic tracks")
        mysteriousPl = Playlist.objects.create(
            name="Mysterious", description="Mysterious tracks")
        romanticPl = Playlist.objects.create(
            name="Romantic", description="Romantic tracks")

        cinematicPl.tracks.add(track1, track2)
        mysteriousPl.tracks.add(track3, track4)
        romanticPl.tracks.add(track5, track56)

        playlists = [cinematicPl, mysteriousPl, romanticPl]
        serializer = PlaylistSerializer(playlists, many=True)

        return JsonResponse(serializer.data, safe=False)
