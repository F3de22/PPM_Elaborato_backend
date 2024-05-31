from django.db import models

# Create your models here.


class Song(models.Model):
    name = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    album = models.CharField(max_length=50, blank=True)
    upload_song = models.FileField(upload_to="media/")
    upload_image = models.ImageField(upload_to="media/")
    data = models.DateTimeField(auto_now=False, auto_now_add=True)
    slug = models.SlugField()


def __str__(self):
    return self.name
