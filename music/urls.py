from django.urls import path, include
from . import views

app_name = 'music'

urlpatterns = [
    path('playlist/', views.playlist, name="playlist"),
    path('', views.createPlaylist, name="createPlaylist"),
    path('', views.searchResults, name="searchResults"),
    path('', views.myPlaylist, name="myPlaylist"),
    path('', views.deletePlaylist, name="deletePlaylist"),
    path('', views.addSongToPlaylist, name="addSongToPlaylist"),
    path('', views.likesong, name="likesong")
]
