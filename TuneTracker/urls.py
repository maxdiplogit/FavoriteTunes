from django.urls import path


from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("songs/", views.song_list, name="song_list"),
    path("songs/add/", views.add_song, name="add_song"),
    path("songs/del_song/<int:song_id>/", views.del_song, name="del_song"),
    path("songs/song_exists", views.song_exists, name="song_exists"),
    path("songs/<int:song_id>/", views.song_detail, name="song_detail")
]
