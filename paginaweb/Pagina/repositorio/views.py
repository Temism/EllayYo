from django.shortcuts import render, redirect,get_object_or_404
from django.http import JsonResponse
from .models import usuario


def index(request):
    return render(request,'vistas/index.html') 

def nueva_cuenta(request):
    return render(request, 'vistas/nueva_cuenta.html')

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

def lista_usuario(request):
    print("estamos en listar")
    usuarios = usuario.objects.all()
    return render(request,'vistas/crud/lista_usuario.html',{"usuarios": usuarios})

def crear_usuario(request):
    print("estamos en crear")
    return render(request,'vistas/crud/crear_usuario.html')

def editar_usuario(request):
    print("estamos en editar")
    return render(request,'vistas/crud/editar_usuario.html')

def crear_u(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        email = request.POST.get("email")
        password = request.POST.get("password")
        if not nombre or not email or not password:
            usuarios = usuario.objects.all()
            return render(request, 'vistas/crud/crear_usuario.html', {"usuarios": usuarios})
        
        nuevo_usuario = usuario.objects.create(nombre=nombre, email=email, password=password)
        nuevo_usuario.save()

        
        return redirect('lista_usuario')
    
    usuarios = usuario.objects.all()
    users = {"usuarios": usuarios}
    return render(request, 'vistas/crud/crear_usuario.html', users)



def borrar_u(request,pk):
    try:
        usuarios = usuario.objects.get(primary=pk)
        usuarios.delete()
        usuarios = usuario.objects.all()
        return redirect('lista_usuario')
    except:
        usuarios = usuario.objects.all()
        return render(request,'vistas/crud/lista_usuario.html',{"usuarios": usuarios})

def editar_u(request, pk):
    user = get_object_or_404(usuario, pk=pk)

    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user.nombre = nombre
        user.email = email
        user.password = password
        user.save()  

        return redirect('lista_usuario')  
    else:
        context = {
            'usuario': user,  
        }
        return render(request, 'vistas/crud/editar_usuario.html', context)
    
    
    

# Create your views here.
