from django.urls import path, include
from . import views

app_name = 'music'

urlpatterns = [
    path('', views.playlist, name="playlist"),
    path('<slug:slug>', views.song_page, name="songpage"),
]
