from django.shortcuts import render, redirect
from django.http import HttpResponse
import hashlib

# Models
from .models import Song, Artist


# Create your views here.
def index(request):
    return render(request, 'home.html')


def song_list(request):
    songs = Song.objects.all()
    
    my_dict = {}
    
    for song in songs:
        artist_name = song.artist.name
        if artist_name in my_dict:
            my_dict[artist_name]['count'] += 1
        else:
            my_dict[artist_name] = { 'count': 1 }
            artist = Artist.objects.get(name = artist_name)
            my_dict[artist_name]['color'] = artist.color
    
    print(my_dict)
    
    return render(request, 'song_list.html', { 'songs': songs, 'feature': my_dict })


def song_detail(request, song_id):
    song = Song.objects.get(id = song_id)
    return render(request, 'song_detail.html', { 'song': song })


def add_song(request):
    if request.method == 'POST':
        song_name = request.POST.get('song').lower()
        artist_name = request.POST.get('artist').lower()
        
        artist = None
        
        # Check if the pair already exists
        try:
            artist = Artist.objects.get(name = artist_name)
            try:
                song = Song.objects.get(title = song_name, artist = artist)
                return redirect('song_exists')
            except Song.DoesNotExist:
                new_song = Song(title = song_name, artist = artist)
                new_song.save()
        except Artist.DoesNotExist or (artist is None):
            color = '#' + hashlib.md5(artist_name.encode('utf-8')).hexdigest()[:6]
            new_artist = Artist(name = artist_name, color = color)
            new_artist.save()
            new_song = Song(title = song_name, artist = new_artist)
            new_song.save()
            
        return redirect('song_list')
    else:
        return render(request, 'add_song.html')


def del_song(request, song_id):
    if request.method == 'POST':
        song = Song.objects.get(id = song_id)
        song.delete()
    return redirect('song_list')


def song_exists(request):
    return render(request, 'song_exists.html')