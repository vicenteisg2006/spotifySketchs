from django.urls import path
from . import views

#urls que reconoce la app
urlpatterns = [
    #principal
    path('', views.loginPage, name='login'),        

    #genericos
    path('artist/', views.artistPage, name='artist'),
    path('user/', views.userPage, name='user'),
    path('dashboard/', views.admin, name='dashboard'),

    #Variantes (Usan alguna base)
    path('userV/', views.userV, name='userV'),
    path('playlistV/', views.playlistV, name='playlistV'),
    path('artistV/', views.artistV, name='artistV'),
    path('artist-songs/', views.artist_songs, name='artist_songs'),

    #playlist
    path('playlist/', views.playlist, name='playlist'),

    #prototipos
    path('Anne-Marie/', views.annemarie, name='AnneMarie'),

    # crear playlist
    path('create-playlist/', views.create_playlist, name='create_playlist'),
    path('add-song/', views.add_song, name='add_song'),
    path('remove-song/', views.remove_song, name='remove_song'),
]