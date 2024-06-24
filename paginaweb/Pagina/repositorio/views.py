from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request,'vistas/index.html') 

def nueva_cuenta(request):
    return render(request,'vistas/nueva_cuenta.html')

def carrito(request):
    return render(request,'vistas/carrito.html')

def contacto(request):
    return render(request,'vistas/contacto.html')

def login(request):
    return render(request,'vistas/login.html')

def sobrenosotros(request):
    return render(request,'vistas/sobrenosotros.html')

def artistas(request):
    return render(request,'vistas/views/artistas.html')


def artista1(request):
    return render(request,'vistas/views/artista1.html')



# Create your views here.
