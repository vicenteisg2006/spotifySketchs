from django.shortcuts import render

# Create your views here.

def loginPage(request):
    return render(request, 'login.html')


def artistPage(request):
    return render(request, 'artist.html')

def userPage(request):
    return render(request, 'user.html')
