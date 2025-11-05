from django.db import models

class Song(models.Model):
    song_text = models.CharField(max_length=300, unique=True)
    img_src = models.URLField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.song_text
    
    class Meta:
        ordering = ['song_text']

class Playlist(models.Model):
    name = models.CharField(max_length=150)
    img_src = models.URLField(max_length=500, default='https://picsum.photos/seed/playlist/300')
    songs = models.ManyToManyField(Song, related_name='playlists', blank=True, through='PlaylistSong')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-created_at']

class PlaylistSong(models.Model):
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ('playlist', 'song')
        ordering = ['order', 'added_at']
    
    def __str__(self):
        return f"{self.song.song_text} en {self.playlist.name}"

