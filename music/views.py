from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .models import Song, Playlist


def playlist(request, playlist_id):
    user = request.user
    if user.is_authenticated:
        myPlaylists = Playlist.objects.filter(user=user)
        if request.method == "POST":
            song_id = request.POST["music_id"]
            playlist = Playlist.objects.filter(playlist_id=playlist_id).first()
            if song_id in playlist.songs.all():
                playlist.songs.remove(song_id)
                playlist.plays -= 1
                playlist.save()
        else:
            currPlaylist = Playlist.objects.filter(playlist_id=playlist_id).first()
            playlistSongs = currPlaylist.songs.all()
            recommendedSingers = []
            return render(request, "music/playlist.html", {'playlistInfo': currPlaylist,
                                                           'playlistSongs': playlistSongs,
                                                           'myPlaylists': myPlaylists,
                                                           'recommendedSingers': recommendedSingers})


def createPlaylist(request):
    user = request.user
    if(user.is_authenticated):
        playlist_name = request.POST["playlist_name"]
        print(f"User: {user}")
        print(f"Playlist Name: {playlist_name}")
        image = request.FILES.get("image")
        newplaylist = Playlist(user=user, playlist_name=playlist_name, image=image)
        newplaylist.save()
        return redirect("music:playlist", playlist_id=newplaylist.playlist_id)
    else:
        return redirect("users:login")


def all_songs(request):
    user = request.user
    genre = request.GET.get('genre')
    if genre:
        allsongs = Song.objects.filter(genre=genre)
    else:
        allsongs = Song.objects.all()
    genres = Song.GENRE_CHOICES

    all_liked = request.user.liked_songs.all()

    if user.is_authenticated:
        my_playlists = Playlist.objects.filter(user=user)
        return render(request, 'music/allsongs.html', {'allsongs': allsongs, 'my_playlists': my_playlists, 'genres': genres, 'all_liked': all_liked})
    else:
        return render(request, 'music/allsongs.html', {'allsongs': allsongs, 'genres': genres})


def search_results(request):
    user = request.user
    myPlaylists = []
    all_liked = request.user.liked_songs.all()
    if user.is_authenticated:
        myPlaylists = list(Playlist.objects.filter(user=user))
    if request.method == "POST":
        data = request.POST["data"]
        songsFound = Song.objects.filter(name__icontains=data)
        playlistsFound = Playlist.objects.filter(playlist_name__icontains=data)
        songsFound = list(songsFound)[:6]
        return render(request, 'music/searchResults.html',
                      {'songsFound': songsFound, 'playlistsFound': playlistsFound, 'all_liked': all_liked, 'myPlaylists': myPlaylists})
    else:
        return redirect('/')


def deletePlaylist(request):
    if request.method == "POST":
        playlist_id = request.POST["playlist_id"]
        Playlist.objects.filter(playlist_id=playlist_id).delete()
    return redirect("/")


def addSongToPlaylist(request):
    user = request.user
    if user.is_authenticated:
        if request.method == "POST":
            song_id = request.POST.get('song_id')
            playlist_id = request.POST.get('playlist_id')
            if song_id and playlist_id:
                song = Song.objects.get(song_id=song_id)
                playlist = Playlist.objects.get(playlist_id=playlist_id)
                if song not in playlist.songs.all():
                    playlist.songs.add(song)
                    playlist.plays = playlist.songs.count()
                    playlist.save()
        return redirect('homepage')


def delete_song_from_playlist(request):
    if request.method == 'POST':
        song_id = request.POST.get('song_id')
        playlist_id = request.POST.get('playlist_id')
        if song_id and playlist_id:
            playlist = get_object_or_404(Playlist, pk=playlist_id)
            song = get_object_or_404(Song, pk=song_id)
            playlist.songs.remove(song)
            playlist.plays = playlist.songs.count()
            playlist.save()
        return redirect('music:playlist', playlist_id=playlist_id)
    return redirect('music:playlist')


def modify_playlist_image(request, playlist_id):
    if request.method == 'POST':
        playlist = get_object_or_404(Playlist, playlist_id=playlist_id)
        if 'image' in request.FILES:
            playlist.image = request.FILES['image']
            playlist.save()
    return redirect('music:playlist', playlist_id=playlist_id)


def add_song(request):
    if request.method == 'POST':
        name = request.POST["name"]
        artist = request.POST["artist"]
        song = request.FILES.get("song")
        genre = request.POST.get("genre")
        image = request.FILES.get("image")
        newsong = Song(name=name, artist=artist, song=song, image=image, genre=genre)
        newsong.save()
        return redirect("homepage")


def likedsongs(request):
    user = request.user
    if user.is_authenticated:
        all_liked = request.user.liked_songs.all()
        return render(request, 'music/likedsongs.html', {'all_liked': all_liked})


def likesong(request):
    user = request.user
    if user.is_authenticated:
        if request.method == "POST":
            song_id = request.POST.get('song_id')
            state = request.POST.get('state')
            song = get_object_or_404(Song, song_id=song_id)
            if state == 'liked':
                if song.liked_by_users.filter(id=user.id).exists():
                    user.liked_songs.remove(song)
            else:
                user.liked_songs.add(song)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


