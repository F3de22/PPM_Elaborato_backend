from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Song, Playlist, LikedSong
from django.contrib import messages
from django.db.models import Case, When
import json
import os


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
            message = "Successfull"
            print(message)
            return HttpResponse(json.dumps({'message': message}))
        else:
            images = os.listdir("media/playlist_images")
            currPlaylist = Playlist.objects.filter(playlist_id=playlist_id).first()
            songs = currPlaylist.songs
            playlistSongs = [currPlaylist.songs.all()]
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
    allsongs = Song.objects.all()
    user = request.user
    if user.is_authenticated:
        my_playlists = Playlist.objects.filter(user=user)
    return render(request, 'music/allsongs.html', {'allsongs': allsongs, 'my_playlists': my_playlists})


def search_results(request):
    user = request.user
    myPlaylists = []
    if user.is_authenticated:
        # Extracting Playlists of the Authenticated User
        myPlaylists = list(Playlist.objects.filter(user=user))
    if request.method == "POST":
        data = request.POST["data"]
        print(f"Search term: {data}")
        songsFound = Song.objects.filter(name__icontains=data)
        print(f"Songs found by name: {songsFound}")
        songsFound = list(songsFound)[:6]
        print(f"Total songs found: {songsFound}")

        return render(request, 'music/searchResults.html',
                      {'songsFound': songsFound, 'myPlaylists': myPlaylists})
    else:
        return redirect("/")


def deletePlaylist(request):
    if request.method == "POST":
        playlist_id = request.POST["playlist_id"]
        Playlist.objects.filter(playlist_id=playlist_id).delete()
        messages.info(request, "Playlist Deleted")
    return redirect("/")


def addSongToPlaylist(request):
    user = request.user
    if request.method == "POST" and request.user.is_authenticated:
        data = request.POST['data']
        if data:
            song_id, playlist_id = data.split("|")
            song_id = song_id[0][2:]
            playlist_id = playlist_id[1][2:]
            currPlaylist = Playlist.objects.filter(playlist_id=playlist_id).first()
            song = Song.objects.filter(song_id=song_id).first()
            if song not in currPlaylist.songs.all():
                currPlaylist.songs.add(song)
                currPlaylist.plays = currPlaylist.songs.count()
                currPlaylist.save()
            return HttpResponse("Successfull")
    else:
        return redirect("users:login")


def likesong(request):
    myPlaylists = []
    user = request.user
    if user.is_authenticated:
        myPlaylists = list(Playlist.objects.filter(user=user))
        if request.method == "POST":
            song_id = request.POST["music_id"]
            isPresent = False
            if LikedSong.objects.filter(user=user, music_id=song_id).exists():
                isPresent = True
            if isPresent:
                LikedSong.objects.filter(user=user, music_id=song_id).delete()
            else:
                like = LikedSong(user=user, music_id=song_id)
                like.save()
                message = "Successfull"
                return HttpResponse(json.dumps({'message': message}))
        else:
            like = LikedSong.objects.filter(user=user)
            ids = []
            for i in like:
                ids.append(i.music_id)
            preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(ids)])
            likedSongs = Song.objects.filter(song_id__in=ids).order_by(preserved)
            return render(request, "music/likedsongs.html", {'likedSongs': likedSongs})
    else:
        return redirect("/")
