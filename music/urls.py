from django.urls import path, include
from . import views

app_name = 'music'

urlpatterns = [
    path('playlist/', views.playlist, name="playlist"),
    path('', views.create_playlist, name="createPlaylist"),
    path('', views.search_results, name="searchResults"),
    path('', views.myPlaylist, name="myPlaylist"),
    path('all_songs/', views.all_songs, name="allsongs"),
    path('homepage/', views.song_list, name="song_list"),
    path('', views.deletePlaylist, name="deletePlaylist"),
    path('', views.addSongToPlaylist, name="addSongToPlaylist"),
    path('', views.likesong, name="likesong"),
    path('example/', views.example, name="example")
]
