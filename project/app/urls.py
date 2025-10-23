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

    #jose tomas henriquez
    path('playlist/', views.playlist, name='playlist'),

    #prototipos
    path('Anne-Marie/', views.annemarie, name='AnneMarie'),

]