from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    return render(request, 'homepage.html')


def profile(request):
    return HttpResponse("that's the profile page")
