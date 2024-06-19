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
    path('likedsongs/', views.likesong, name="likedsongs"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
