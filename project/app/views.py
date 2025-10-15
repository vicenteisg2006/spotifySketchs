from django.shortcuts import render, redirect

# Create your views here.

def loginPage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        if username == "user" and password == "user123":
            return redirect("user")
        elif username == "artist" and password == "artist123":
            return redirect("artist")
        elif username == "admin" and password == "admin123":
            return redirect("admin")
        else:
            error_msg = "Invalid credentials, please try again."
            return render(request, "login.html", {"error": error_msg})

    return render(request, 'login.html')


def artistPage(request):
    return render(request, 'artist.html')

def userPage(request):
    return render(request, 'user.html')

def ejemplo(request):
    return render(request, 'ejercicio10.html')

def admin(request):
    return render(request, 'admin.html')
