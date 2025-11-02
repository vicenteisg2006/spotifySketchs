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
        'streams_chart': json.dumps(streams_chart), #jsoneado
        'continental_data': json.dumps(continental_data), #jsoneado
    }
    return render(request, '0_artist_v.html', context)


def annemarie(request): #prototipo vicente 
    return render(request, 'am.html')






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