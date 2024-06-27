from django.shortcuts import render
from django.http import HttpResponse
from .models import usuarios


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

def artista2(request):
    return render(request,'vistas/views/artista2.html')

def artista3(request):
    return render(request,'vistas/views/artista3.html')

def artista4(request):
    return render(request,'vistas/views/artista4.html')

def detalle1(request):
    return render(request,'vistas/views/detalle1.html')

def detalle2(request):
    return render(request,'vistas/views/detalle2.html')

def detalle3(request):
    return render(request,'vistas/views/detalle3.html')

def detalle4(request):
    return render(request,'vistas/views/detalle4.html')





def usuarios(request):
    users= usuarios.objects.all()
    datos = {'usuarios' : users}
    return render(request, 'vistas/usuariocrear.html', datos)

# Create your views here.
