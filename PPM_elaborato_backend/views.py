from django.http import HttpResponse
from django.shortcuts import render
from music.models import Song


def homepage(request):
    songs = Song.objects.all()
    return render(request, 'homepage.html', {'songs': songs})


def profile(request):
    return HttpResponse("that's the profile page")
