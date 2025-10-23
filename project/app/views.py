from django.shortcuts import render, redirect


#Login
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
        
        else:
            error_msg = "Invalid credentials, please try again."
            return render(request, "login.html", {"error": error_msg})

    return render(request, 'login.html')

#Artista generico
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

#Usuario
def userPage(request):
    return render(request, 'user.html')

#Administrador
def admin(request):
    return render(request, 'admin.html')


#Playlist
def playlist(request):
    return render(request, 'playlist.html')

#prototipos

#vicente 
def annemarie(request):
    return render(request, 'am.html')

from django.shortcuts import render

