from django import forms 
from.models import usuarios

from django.forms import ModelForm

class usuarioform(ModelForm):
    class Meta:
        Model = usuarios
        fields ="__all__"