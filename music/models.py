from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

# Create your models here.


class Song(models.Model):
    song_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    album = models.CharField(max_length=50, blank=True)
    song = models.FileField(upload_to="media/songs/", validators=[FileExtensionValidator(allowed_extensions=['mp3', 'wav'])], default="name")
    image = models.ImageField(upload_to="media/songimage/", validators=[FileExtensionValidator(allowed_extensions=['jpeg', 'jpg', 'png'])], default="https://placehold.co/300x300/png")
    data = models.DateTimeField(auto_now=False, auto_now_add=True)
    slug = models.SlugField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Playlist(models.Model):
    playlist_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default="name")
    image = models.ImageField(upload_to="media/images/", validators=[FileExtensionValidator(allowed_extensions=['jpeg', 'jpg', 'png'])])
    slug = models.SlugField()

    def __str__(self):
        return self.user.first_name


class LikedSong(models.Model):
    liked_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    music_id = models.CharField(max_length=50, default="name")

    def __str__(self):
        return self.user.first_name
