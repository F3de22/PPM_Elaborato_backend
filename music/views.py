from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Song, Playlist, LikedSong
from django.contrib import messages
from django.db.models import Case, When
import json
import os


# Create your views here.

def playlist(request):
    play_list = Song.objects.all()
    return render(request, 'music/playlist.html', {'playlist': play_list})


def song_list(request):
    songs = Song.objects.all()
    print('My songs are', songs)
    return render(request, 'homepage.html', {'songs': songs})


def createPlaylist(request):
    user = request.user
    if(user.is_authenticated):
        playlist_name = request.POST["playlist_name"]
        print(f"User: {user}")
        print(f"Playlist Name: {playlist_name}")
        newplaylist = Playlist(user=user, playlist_name=playlist_name)
        newplaylist.save()
        print(f"New Playlist Created: {newplaylist.playlist_id}")
        return redirect("music:playlist")
    else:
        return redirect("users:login")



def all_songs(request):
    allsongs = Song.objects.all()
    print(allsongs)
    return render(request, 'music/allsongs.html', {'allsongs': allsongs})


def search_results(request):
    user = request.user
    myPlaylists = []
    if user.is_authenticated:
        # Extracting Playlists of the Authenticated User
        myPlaylists = list(Playlist.objects.filter(user=user))
    if request.method == "POST":
        data = request.POST["data"]
        allSongs = Song.objects.all()
        songsFound = allSongs.filter(name__icontains=data)
        moviesFound = allSongs.filter(movie__icontains=data)
        songsFound = list(set(list(songsFound) + list(moviesFound)))[:6]

        return render(request, 'searchResults.html',
                      {'songsFound': songsFound, 'myPlaylists': myPlaylists})
    else:
        return redirect("/")


def playlist(request, id):
    user = request.user
    if user.is_authenticated:
        myPlaylists = list(Playlist.objects.filter(user=user))
        if request.method == "POST":
            song_id = request.POST["music_id"]
            playlist = Playlist.objects.filter(playlist_id=id).first()
            if song_id in playlist.music_ids:
                playlist.music_ids.remove(song_id)
                playlist.plays -= 1
                playlist.save()
            message = "Successfull"
            print(message)
            return HttpResponse(json.dumps({'message': message}))
        else:
            images = os.listdir("media/playlist_images")
            print(images)
            currPlaylist = Playlist.objects.filter(playlist_id=id).first()
            music_ids = currPlaylist.music_ids
            playlistSongs = []
            recommendedSingers = []
            for music_id in music_ids:
                song = Song.objects.filter(song_id=music_id).first()
                playlistSongs.append(song)
            return render(request, "music/playlist.html", {'playlistInfo': currPlaylist,
                                                           'playlistSongs': playlistSongs,
                                                           'myPlaylists': myPlaylists,
                                                           'recommendedSingers': recommendedSingers})


def deletePlaylist(request):
    if request.method == "POST":
        playlist_id = request.POST["playlist_id"]
        # print(playlist_id)
        Playlist.objects.filter(playlist_id=playlist_id).delete()
        messages.info(request, "Playlist Deleted")
        print("Playlist Deleted")
    return redirect("/")


def addSongToPlaylist(request):
    user = request.user
    if user.is_authenticated:
        try:
            data = request.POST['data']
            ids = data.split("|")
            song_id = ids[0][2:]
            playlist_id = ids[1][2:]
            print(ids[0][2:], ids[1][2:])
            currPlaylist = Playlist.objects.filter(playlist_id=playlist_id).first()
            if song_id not in currPlaylist.music_ids:
                currPlaylist.music_ids.append(song_id)
                currPlaylist.plays = len(currPlaylist.music_ids)
                currPlaylist.save()
            return HttpResponse("Successfull")
        except:
            return redirect("/")
        # return redirect("/")
    else:
        return redirect("/")


def likesong(request):
    myPlaylists = []
    try:
        # print("Request Submitted Successfully!!!")
        user = request.user
        if user.is_authenticated:
            # Extracting Playlists of the Authenticated User
            myPlaylists = list(Playlist.objects.filter(user=user))
        if user.is_authenticated:
            if request.method == "POST":
                song_id = request.POST["music_id"]
                isPresent = False
                if LikedSong.objects.filter(user=user, music_id=song_id).exists():
                    isPresent = True

                if isPresent:
                    LikedSong.objects.filter(user=user, music_id=song_id).delete()
                    # print(f"Your song is removed from the liked song id: {song_id}")
                else:
                    like = LikedSong(user=user, music_id=song_id)
                    like.save()
                    # print(f"Your song successfully added id: {song_id}")
                message = "Successfull"
                return HttpResponse(json.dumps({'message': message}))
            else:
                like = LikedSong.objects.filter(user=user)
                ids = []
                for i in like:
                    ids.append(i.music_id)
                preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(ids)])
                likedSongs = Song.objects.filter(song_id__in=ids).order_by(preserved)
                return render(request, "likedSong.html", {'likedSongs': likedSongs})
        else:
            # print("User is not authenticated")
            return redirect("/")
    except:
        return redirect("/")
