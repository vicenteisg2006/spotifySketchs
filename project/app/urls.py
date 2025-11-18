from django.urls import path
from . import views

#urls que reconoce la app
urlpatterns = [
    #principal
    path('', views.loginPage, name='login'),        

    #genericos
    path('artist/', views.artistPage, name='artist'),         ## BORRAR
    path('user/', views.userPage, name='user'),             ## BORRAR
    path('dashboard/', views.admin, name='dashboard'),

    #Variantes (Usan alguna base)
    path('userV/<int:perfil_id>', views.userV, name='userV'),      ##
    path('playlistV/<int:perfil_id>', views.playlistV, name='playlistV'),
    path('artistV/<int:perfil_id>', views.artistV, name='artistV'),
    path('artist-songs/<int:perfil_id>', views.artist_songs, name='artist_songs'),

    path('moder/<int:perfil_id>', views.moder, name='moder'),
    path('funcionAlert/<int:perfil_id>', views.alert, name='alert'),
    path('funcionBan/<int:perfil_id>', views.moderate, name='moderate'),
    path('moderador/data/<str:chart_id>/', views.get_moder_data, name='moder_data'),

    path('prueba/', views.prueba, name='prueba'),  #Prueba


    #playlist
    path('playlist/', views.playlist, name='playlist'),

    #prototipos
    path('Anne-Marie/', views.annemarie, name='AnneMarie'),      ## BORRAR

    # crear playlist
    path('create-playlist/', views.create_playlist, name='create_playlist'),
    path('add-song/', views.add_song, name='add_song'),
    path('remove-song/', views.remove_song, name='remove_song'),
]