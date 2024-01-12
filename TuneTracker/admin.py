from django import forms
from django.contrib import admin


# Register your models here.
from .models import Artist, Song


class ArtistAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        existing_artist = Artist.objects.filter(name=obj.name).exclude(pk=obj.pk)
        if existing_artist.exists():
            raise forms.ValidationError('Artist with this name already exists.')
        obj.save()


class SongAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        existing_song = Song.objects.filter(title=obj.title, artist=obj.artist).exclude(pk=obj.pk)
        if existing_song.exists():
            raise forms.ValidationError('Song with this title and artist already exists.')
        obj.save()


admin.site.register(Artist, ArtistAdmin)
admin.site.register(Song, SongAdmin)