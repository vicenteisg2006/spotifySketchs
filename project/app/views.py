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
    return render(request, 'artist.html')

#Usuario
def userPage(request):
    return render(request, 'user.html')

#Administrador
def admin(request):
    return render(request, 'admin.html')


#jose tomas henriquez
def playlist(request):
    return render(request, 'playlist.html')

#prototipos

#vicente 
def annemarie(request):
    return render(request, 'am.html')