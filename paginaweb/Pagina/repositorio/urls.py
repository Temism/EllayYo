from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Index.html', views.index, name='index'),
    path('carrito.html', views.carrito, name='carrito'),
    path('contacto.html', views.contacto, name='contacto'),
    path('login.html', views.login, name='login'),
    path('nueva_cuenta.html', views.nueva_cuenta, name='nueva_cuenta'),
    path('Sobrenosotros.html', views.sobrenosotros, name='sobrenosotros'),
    path('views/artistas.html',views.artistas, name='artistas'),
    path('views/artista1.html',views.artista1, name='artista1'),
    path('views/artista2.html',views.artista2, name='artista2'),
    path('views/artista3.html',views.artista3, name='artista3'),
    path('views/artista4.html',views.artista4, name='artista4'),
    path('views/detalle1.html',views.detalle1, name='detalle1'),
    path('views/detalle2.html',views.detalle2, name='detalle2'),
    path('views/detalle3.html',views.detalle3, name='detalle3'),
    path('views/detalle4.html',views.detalle4, name='detalle4'),
    path('usuariocrear.html',views.usuarios,name='usuarioscrear'),
]
