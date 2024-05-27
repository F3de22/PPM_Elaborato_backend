from django.db import models

# Create your models here.


class Song(models.Model):
    name = models.CharField(max_length=50)
    time = models.TimeField
    artist = models.CharField(max_length=50)
    data = models.DateTimeField(auto_now=False, auto_now_add=True)
    slug = models.SlugField()


def __str__(self):
    return self.titolo
