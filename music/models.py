from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Song(models.Model):
    song_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    album = models.CharField(max_length=50, blank=True)
    song = models.FileField(upload_to="media/songs/")
    image = models.ImageField(upload_to="media/images/")
    data = models.DateTimeField(auto_now=False, auto_now_add=True)
    slug = models.SlugField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Playlist(models.Model):
    playlist_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default="")
    image = models.ImageField(upload_to="media/images/")
    slug = models.SlugField()

    def __str__(self):
        return self.user.first_name


class LikedSong(models.Model):
    liked_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    music_id = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.user.first_name