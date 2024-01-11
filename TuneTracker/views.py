from django.shortcuts import render
from django.http import HttpResponse;

# Models
from .models import Song


# Create your views here.
def index(request):
    return HttpResponse("Hello world")


def song_list(request):
    songs = Song.objects.all()
    return render(request, 'song_list.html', { 'songs': songs })


def song_detail(request, song_id):
    song = Song.objects.get(id=song_id)
    return render(request, 'song_detail.html', { 'song': song })