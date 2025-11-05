from django.shortcuts import render, redirect
from django.http import JsonResponse
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
        'values': [120000, 150000, 170000, 190000, 210000, 260000, 300000],
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

    #context
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
        'top_viewers': [
            {'name': 'User1', 'streams': 15000},
            {'name': 'User2', 'streams': 12000},
            {'name': 'User3', 'streams': 10000},
            {'name': 'User4', 'streams': 8000},
            {'name': 'User5', 'streams': 5000},
            ],
        'streams_chart': json.dumps(streams_chart), #jsoneado
        'continental_data': json.dumps(continental_data), #jsoneado
    }
    return render(request, '0_artist_v.html', context)


def annemarie(request): #prototipo vicente 
    return render(request, 'am.html')

def artist_songs(request): #Vista de todas las canciones del artista
    context = {
        'artist_name': 'Dua Lipa',
        'total_songs': 45,
        'songs': [
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
        ],
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
    return render(request, '0_playlist_v.html')








# ========== ADMINISTRADOR ==========
def admin(request): #Administrador
    return render(request, 'admin.html')



# ========== COMPLEMENTOS ADMINISTRADOR ==========