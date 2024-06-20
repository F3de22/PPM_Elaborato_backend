from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django import forms


# Create your models here.


class Song(models.Model):
    song_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    album = models.CharField(max_length=50, blank=True)
    genre = models.CharField(max_length=20, blank=True, default='genre')
    song = models.FileField(upload_to="songs/", validators=[FileExtensionValidator(allowed_extensions=['mp3', 'wav'])], default="name")
    image = models.ImageField(upload_to="songimage/", validators=[FileExtensionValidator(allowed_extensions=['jpeg', 'jpg', 'png'])])
    data = models.DateTimeField(auto_now=False, auto_now_add=True)
    slug = models.SlugField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Playlist(models.Model):
    playlist_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    playlist_name = models.CharField(max_length=50, default="name")
    image = models.ImageField(upload_to="playlist_images/", validators=[FileExtensionValidator(allowed_extensions=['jpeg', 'jpg', 'png'])], blank=True)
    plays = models.IntegerField(default=0)
    songs = models.ManyToManyField(Song, related_name='playlist')
    slug = models.SlugField()

    def __str__(self):
        return self.playlist_name


class LikedSong(models.Model):
    liked_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    music_id = models.ForeignKey(Song, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.first_name} - {self.music_id.name}"

