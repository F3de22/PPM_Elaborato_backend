from django.urls import path, include
from . import views

app_name = 'music'

urlpatterns = [
    path('playlist/', views.playlist, name="playlist"),
    path('createPlaylist', views.createPlaylist, name='createPlaylist'),
    path('', views.search_results, name="searchResults"),
    path('allsongs/', views.all_songs, name="allsongs"),
    path('', views.deletePlaylist, name="deletePlaylist"),
    path('', views.addSongToPlaylist, name="addSongToPlaylist"),
    path('likedsongs/', views.likesong, name="likedsongs"),
]
