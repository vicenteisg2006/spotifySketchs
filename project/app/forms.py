from django import forms
from .models import Playlist, Song
from .models import PERFIL, alertaMODERADOR

class PlaylistForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = ['name', 'img_src']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre de la playlist...'
            }),
            'img_src': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'URL de la imagen de la playlist'
            })
        }
        labels = {
            'name': '',
            'img_src': ''
        }

class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['song_text', 'img_src']
        widgets = {
            'song_text': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre de la canción - Artista'
            }),
            'img_src': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'URL de la imagen'
            })
        }
        labels = {
            'song_text': 'Canción',
            'img_src': 'Imagen'
        }

# ========== formularios Vicente ==========
class alertaMODERADORForm(forms.ModelForm):
    receptor = forms.ModelChoiceField(queryset=PERFIL.objects.all())

    class Meta:
        model = alertaMODERADOR
        fields = ['receptor', 'mensajeAlerta']
