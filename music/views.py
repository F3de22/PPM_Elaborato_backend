from django.shortcuts import render
from .models import Song
from django.http import HttpResponse

# Create your views here.


def playlist(request):
    play_list = Song.objects.all().order_by('-date')
    return render(request, 'music/playlist.html', {'playlist': play_list})


def song_page(request, slug):
    song_main = Song.objects.git(slug=slug)
    return render(request, 'music/song_page.html', {'song': song_main})
