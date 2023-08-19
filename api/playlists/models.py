from django.db import models

class Song(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    
class Playlist(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    songs = models.ManyToManyField(Song, related_name='playlists')

    def __str__(self):
        return self.name
