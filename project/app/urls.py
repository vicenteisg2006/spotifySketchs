from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginPage, name='login'),
    path('artist/', views.artistPage, name='artist'),
    path('user/', views.userPage, name='user'),
]