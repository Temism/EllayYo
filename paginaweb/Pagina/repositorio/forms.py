from django import forms 
from.models import usuario

from django.forms import ModelForm

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = usuario
        fields = ['nombre', 'password', 'email']