from django.http import HttpResponse
from django.shortcuts import render
from music.models import Song, Playlist


def homepage(request):
    songs = Song.objects.all()
    user = request.user
    if user.is_authenticated:
        my_playlists = Playlist.objects.filter(user=user)
    return render(request, 'homepage.html', {'songs': songs, 'my_playlists': my_playlists})


def profile(request):
    return HttpResponse("that's the profile page")
