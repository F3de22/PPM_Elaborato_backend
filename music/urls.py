from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'music'

urlpatterns = [
    path('playlist/<int:playlist_id>/', views.playlist, name="playlist"),
    path('createPlaylist', views.createPlaylist, name='createPlaylist'),
    path('searchResults/', views.search_results, name="search_results"),
    path('allsongs/', views.all_songs, name="allsongs"),
    path('deletePlaylist', views.deletePlaylist, name="deletePlaylist"),
    path('addSongToPlaylist', views.addSongToPlaylist, name="addSongToPlaylist"),
    path('modify_playlist_image/<int:playlist_id>', views.modify_playlist_image, name='modify_playlist_image'),
    path('likedsongs/', views.likesong, name="likedsongs"),
    path('add-song', views.add_song, name='add_song'),
    path('delete_song_from_playlist', views.delete_song_from_playlist, name="delete_song_from_playlist"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
