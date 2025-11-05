from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Playlist, Song, PlaylistSong
import json



# ========== LOGIN ==========
def loginPage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")


        #Segun las contraseñas que recibe, redirige a un html
        if username == "user" and password == "user123":
            return redirect("user")                                         #Usuario
        elif username == "artist" and password == "artist123":
            return redirect("artist")                                        #Artista Generico
        elif username == "admin" and password == "admin123":
            return redirect("dashboard")                                  #Administrador
        elif username == "anne-marie" and password == "am123":
            return redirect("AnneMarie")                                   #Anne-Marie
        elif username == "userV" and password == "userV123":
            return redirect("userV")                                       #Variante usuario -> usando BaseK
        elif username == "artistV" and password == "artistV123":
            return redirect("artistV")                                      #Variante artista -> usando BaseKA
        
        #Mensaje de error
        else:
            error_msg = "Invalid credentials, please try again."
            return render(request, "login.html", {"error": error_msg})

    return render(request, 'login.html')







# ========== ARTISTAS ==========
def artistPage(request):
    context = {
        'artist_name': 'Dua Lipa',
        'total_streams': 1234567,
        'monthly_listeners': 456789,
        'followers': 123456,
        'top_songs': [
            {'name': 'Levitating', 'streams': 500000},
            {'name': 'Don’t Start Now', 'streams': 400000},
            {'name': 'Dance the Night', 'streams': 300000},
            {'name': 'New Rules', 'streams': 200000},
            {'name': 'Hallucinate', 'streams': 100000},
            ],
        'streams_chart': {
            'labels': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul'],
            'values': [120000, 150000, 170000, 190000, 210000, 260000, 300000],
            }
        }
    return render(request, 'artist.html', context)

def artistV(request): #Variante artista -> usando BaseKA
    #Datos para jsonear
    streams_chart = {
        'labels': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul'],
        'values': [130000, 150000, 100000, 190000, 210000, 260000, 150000],
    }

    listeners_chart = {
        'labels': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul'],
        'values': [18000, 22500, 25500, 20000, 31500, 32000, 45000],
    }

    continental_data = {
        'Jan': {'Asia': 10000, 'Africa': 10000, 'America': 35000, 'Europa': 40000, 'Oceania': 25000},
        'Feb': {'Asia': 15000, 'Africa': 15000, 'America': 40000, 'Europa': 45000, 'Oceania': 35000},
        'Mar': {'Asia': 20000, 'Africa': 20000, 'America': 45000, 'Europa': 50000, 'Oceania': 35000},
        'Apr': {'Asia': 22000, 'Africa': 21000, 'America': 49000, 'Europa': 60000, 'Oceania': 38000},
        'May': {'Asia': 27000, 'Africa': 21000, 'America': 53000, 'Europa': 64000, 'Oceania': 45000},
        'Jun': {'Asia': 40000, 'Africa': 25000, 'America': 65000, 'Europa': 75000, 'Oceania': 55000},
        'Jul': {'Asia': 45000, 'Africa': 30000, 'America': 80000, 'Europa': 80000, 'Oceania': 65000},
    }

    continental_listeners_data = {
        'Jan': {'Asia': 1500, 'Africa': 1500, 'America': 5250, 'Europa': 6000, 'Oceania': 3750},
        'Feb': {'Asia': 2250, 'Africa': 2250, 'America': 6000, 'Europa': 6750, 'Oceania': 5250},
        'Mar': {'Asia': 3000, 'Africa': 3000, 'America': 6750, 'Europa': 7500, 'Oceania': 5250},
        'Apr': {'Asia': 3300, 'Africa': 3150, 'America': 7350, 'Europa': 9000, 'Oceania': 5700},
        'May': {'Asia': 4050, 'Africa': 3150, 'America': 7950, 'Europa': 9600, 'Oceania': 6750},
        'Jun': {'Asia': 6000, 'Africa': 3750, 'America': 9750, 'Europa': 11250, 'Oceania': 8250},
        'Jul': {'Asia': 6750, 'Africa': 4500, 'America': 12000, 'Europa': 12000, 'Oceania': 9750},
    }

    # Datos de canciones para calcular álbumes más escuchados
    songs = [
        {'name': 'Levitating', 'album': 'Future Nostalgia', 'duration': '3:23', 'streams': 500000, 'release_date': '2020-03-27'},
        {'name': 'Don\'t Start Now', 'album': 'Future Nostalgia', 'duration': '3:03', 'streams': 400000, 'release_date': '2019-11-01'},
        {'name': 'Dance the Night', 'album': 'Barbie The Album', 'duration': '2:57', 'streams': 300000, 'release_date': '2023-05-25'},
        {'name': 'New Rules', 'album': 'Dua Lipa', 'duration': '3:29', 'streams': 200000, 'release_date': '2017-07-07'},
        {'name': 'Hallucinate', 'album': 'Future Nostalgia', 'duration': '3:27', 'streams': 100000, 'release_date': '2020-03-27'},
        {'name': 'Physical', 'album': 'Future Nostalgia', 'duration': '3:13', 'streams': 250000, 'release_date': '2020-01-31'},
        {'name': 'Break My Heart', 'album': 'Future Nostalgia', 'duration': '3:41', 'streams': 180000, 'release_date': '2020-03-25'},
        {'name': 'One Kiss', 'album': 'One Kiss', 'duration': '3:34', 'streams': 350000, 'release_date': '2018-04-06'},
        {'name': 'IDGAF', 'album': 'Dua Lipa', 'duration': '3:38', 'streams': 220000, 'release_date': '2018-01-12'},
        {'name': 'Cold Heart', 'album': 'Cold Heart', 'duration': '3:22', 'streams': 280000, 'release_date': '2021-08-13'},
        {'name': 'Love Again', 'album': 'Future Nostalgia', 'duration': '4:18', 'streams': 150000, 'release_date': '2020-03-27'},
        {'name': 'Pretty Please', 'album': 'Future Nostalgia', 'duration': '3:15', 'streams': 90000, 'release_date': '2020-03-27'},
        {'name': 'Be the One', 'album': 'Dua Lipa', 'duration': '3:23', 'streams': 170000, 'release_date': '2015-10-30'},
        {'name': 'Blow Your Mind', 'album': 'Dua Lipa', 'duration': '3:32', 'streams': 140000, 'release_date': '2016-08-26'},
        {'name': 'Hotter Than Hell', 'album': 'Dua Lipa', 'duration': '3:08', 'streams': 130000, 'release_date': '2016-06-10'},
    ]
    
    # Calcular streams por álbum
    album_streams = {}
    for song in songs:
        album = song['album']
        if album not in album_streams:
            album_streams[album] = 0
        album_streams[album] += song['streams']
    
    # Ordenar álbumes por streams (descendente)
    sorted_albums = sorted(album_streams.items(), key=lambda x: x[1], reverse=True)
    
    albums_chart = {
        'labels': [album[0] for album in sorted_albums],
        'data': [album[1] for album in sorted_albums],
        'backgroundColor': ['#FF6B9D', '#4ECDC4', '#FFD93D', '#95E1D3', '#C77DFF', '#00F5FF'],
    }

    #context
    context = {
        'artist_name': 'Dua Lipa',
        'total_streams': 3460000,
        'monthly_listeners': 456789,
        'followers': 123456,
        'top_songs': [
            {'name': 'Levitating', 'streams': 500000},
            {'name': 'Don\'t Start Now', 'streams': 400000},
            {'name': 'Dance the Night', 'streams': 300000},
            {'name': 'New Rules', 'streams': 200000},
            {'name': 'Hallucinate', 'streams': 100000},
            ],
        'top_viewers': [
            {'name': 'User1', 'streams': 15000},
            {'name': 'User2', 'streams': 12000},
            {'name': 'User3', 'streams': 10000},
            {'name': 'User4', 'streams': 8000},
            {'name': 'User5', 'streams': 5000},
            ],
        'streams_chart': json.dumps(streams_chart), #jsoneado
        'listeners_chart': json.dumps(listeners_chart), #jsoneado
        'continental_data': json.dumps(continental_data), #jsoneado
        'continental_listeners_data': json.dumps(continental_listeners_data), #jsoneado
        'albums_chart': json.dumps(albums_chart), #jsoneado
    }
    return render(request, '0_artist_v.html', context)


def annemarie(request): #prototipo vicente 
    return render(request, 'am.html')

def artist_songs(request): #Vista de todas las canciones del artista
    songs = [
        {'name': 'Levitating', 'album': 'Future Nostalgia', 'duration': '3:23', 'streams': 500000, 'release_date': '2020-03-27'},
        {'name': 'Don\'t Start Now', 'album': 'Future Nostalgia', 'duration': '3:03', 'streams': 400000, 'release_date': '2019-11-01'},
        {'name': 'Dance the Night', 'album': 'Barbie The Album', 'duration': '2:57', 'streams': 300000, 'release_date': '2023-05-25'},
        {'name': 'New Rules', 'album': 'Dua Lipa', 'duration': '3:29', 'streams': 200000, 'release_date': '2017-07-07'},
        {'name': 'Hallucinate', 'album': 'Future Nostalgia', 'duration': '3:27', 'streams': 100000, 'release_date': '2020-03-27'},
        {'name': 'Physical', 'album': 'Future Nostalgia', 'duration': '3:13', 'streams': 250000, 'release_date': '2020-01-31'},
        {'name': 'Break My Heart', 'album': 'Future Nostalgia', 'duration': '3:41', 'streams': 180000, 'release_date': '2020-03-25'},
        {'name': 'One Kiss', 'album': 'One Kiss', 'duration': '3:34', 'streams': 350000, 'release_date': '2018-04-06'},
        {'name': 'IDGAF', 'album': 'Dua Lipa', 'duration': '3:38', 'streams': 220000, 'release_date': '2018-01-12'},
        {'name': 'Cold Heart', 'album': 'Cold Heart', 'duration': '3:22', 'streams': 280000, 'release_date': '2021-08-13'},
        {'name': 'Love Again', 'album': 'Future Nostalgia', 'duration': '4:18', 'streams': 150000, 'release_date': '2020-03-27'},
        {'name': 'Pretty Please', 'album': 'Future Nostalgia', 'duration': '3:15', 'streams': 90000, 'release_date': '2020-03-27'},
        {'name': 'Be the One', 'album': 'Dua Lipa', 'duration': '3:23', 'streams': 170000, 'release_date': '2015-10-30'},
        {'name': 'Blow Your Mind', 'album': 'Dua Lipa', 'duration': '3:32', 'streams': 140000, 'release_date': '2016-08-26'},
        {'name': 'Hotter Than Hell', 'album': 'Dua Lipa', 'duration': '3:08', 'streams': 130000, 'release_date': '2016-06-10'},
    ]
    
    # Calcular el total de streams sumando todos los streams de las canciones
    total_streams = sum(song['streams'] for song in songs)
    
    context = {
        'artist_name': 'Dua Lipa',
        'total_songs': len(songs),
        'total_streams': total_streams,
        'songs': songs,
    }
    return render(request, 'artist_songs.html', context)






# ========== USUARIOS ==========
def userPage(request): #Inicial
    return render(request, 'user.html')

def userV(request): #Variante -> usando BaseK
    return render(request, '0_user_v.html')







# ========== COMPLEMENTOS USUARIOS ==========
def playlist(request): #Playlist
    return render(request, 'playlist.html')

def playlistV(request): #Variante playlist -> usando BaseK
    # Verificar si se está cargando una playlist específica desde la galería
    load_playlist_id = request.GET.get('playlist_id')
    
    if load_playlist_id:
        # Si se pasa un ID por GET, cargar esa playlist
        request.session['active_playlist_id'] = int(load_playlist_id)
    
    # Obtener la playlist activa de la sesión (si existe)
    playlist_id = request.session.get('active_playlist_id')
    playlist_obj = None
    songs_list = []
    
    if playlist_id:
        try:
            playlist_obj = Playlist.objects.get(id=playlist_id)
            # Obtener todas las canciones de la playlist con su información
            songs_list = list(playlist_obj.songs.values('id', 'song_text', 'img_src'))
        except Playlist.DoesNotExist:
            request.session.pop('active_playlist_id', None)
    
    # Obtener todas las playlists para mostrar en la galería
    all_playlists = Playlist.objects.all()
    
    context = {
        'placeholder_text': 'Ingresa el nombre de tu playlist',
        'playlist_name': playlist_obj.name if playlist_obj else None,
        'songs': json.dumps(songs_list),
        'all_playlists': all_playlists
    }
    return render(request, '0_playlist_v.html', context)








# ========== ADMINISTRADOR ==========
def admin(request): #Administrador
    return render(request, 'admin.html')



# ========== COMPLEMENTOS ADMINISTRADOR ==========


# ========== PLAYLIST ==========
def create_playlist(request):
    if request.method == "POST":
        playlist_name = request.POST.get("playlist_name")
        img_src = request.POST.get("img_src")
        
        # Si no se proporciona imagen, usar una por defecto
        if not img_src:
            img_src = "/static/images/playlist1.jpg"
        
        # Crear la playlist en la base de datos
        playlist_obj = Playlist.objects.create(name=playlist_name, img_src=img_src)
        
        # Guardar el ID de la playlist en la sesión
        request.session['active_playlist_id'] = playlist_obj.id
        
        return redirect('playlistV')
    
    return redirect('playlistV')

def add_song(request):
    if request.method == "POST":
        playlist_id = request.session.get('active_playlist_id')
        
        if not playlist_id:
            return JsonResponse({'error': 'No hay playlist activa'}, status=400)
        
        try:
            playlist_obj = Playlist.objects.get(id=playlist_id)
            song_text = request.POST.get('song_text')
            img_src = request.POST.get('img_src')
            
            # Crear o obtener la canción (puede existir en otras playlists)
            song, created = Song.objects.get_or_create(
                song_text=song_text,
                defaults={'img_src': img_src}
            )
            
            # Actualizar img_src si la canción ya existía pero con otra imagen
            if not created and song.img_src != img_src:
                song.img_src = img_src
                song.save()
            
            # Verificar si la canción ya está en esta playlist
            if playlist_obj.songs.filter(id=song.id).exists():
                return JsonResponse({'error': 'La canción ya existe en la playlist'}, status=400)
            
            # Agregar la canción a la playlist
            playlist_obj.songs.add(song)
            
            return JsonResponse({
                'success': True,
                'song_id': song.id,
                'song_text': song.song_text,
                'img_src': song.img_src
            })
            
        except Playlist.DoesNotExist:
            return JsonResponse({'error': 'Playlist no encontrada'}, status=404)
    
    return JsonResponse({'error': 'Método no permitido'}, status=405)

def remove_song(request):
    if request.method == "POST":
        song_id = request.POST.get('song_id')
        playlist_id = request.session.get('active_playlist_id')
        
        if not playlist_id:
            return JsonResponse({'error': 'No hay playlist activa'}, status=400)
        
        try:
            playlist_obj = Playlist.objects.get(id=playlist_id)
            song = Song.objects.get(id=song_id)
            
            # Remover la canción de la playlist (no la elimina de la BD)
            playlist_obj.songs.remove(song)
            
            return JsonResponse({'success': True})
        except Playlist.DoesNotExist:
            return JsonResponse({'error': 'Playlist no encontrada'}, status=404)
        except Song.DoesNotExist:
            return JsonResponse({'error': 'Canción no encontrada'}, status=404)
    
    return JsonResponse({'error': 'Método no permitido'}, status=405)
