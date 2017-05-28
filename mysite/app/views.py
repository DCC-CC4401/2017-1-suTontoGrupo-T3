# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .forms import LoginForm
from .models import *
from django.contrib import auth


def index(request):
    return render(request, 'app/index.html')


def login(request):
    form = LoginForm(request.POST)
    # formulario lleno, edicion de datos
    if request.method == 'POST' and form.is_valid():
        # obtengo mail y pass
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        # veo si estan en la bd
        if UserInfo.objects.get(user=username) != None:
            auth.login(request, username)
            usuario = UserInfo.objects.get(user=username)
            if usuario.tipo == 'vendedor':
                return render(request, 'app/vendedor_profile.html', {'usuario': usuario})
            else:
                return render(request, 'app/vendedor_profileAlumno.html', {'usuario': usuario})
    else:
        form = LoginForm()

    return render(request, 'app/login.html', {'form': form})


def gestion_productos(request):
    return render(request, 'app/gestion_productos.html')


def home(request):
    return render(request, 'app/home.html')


def signup(request):
    return render(request, 'app/signup.html')


# informacion de test
pizza = {'nombre': 'Pizza',
         'precio': '$1.300',
         'descripcion': 'Deliciosa pizza hecha con masa casera, viene disponible en 3 tipos.',
         'categoria': 'Almuerzos',
         'stock': 20,
         'icono': "../../static/img/pizza.png",
         'imagen': "#modal1"}

pepperoni = {'descripcion': '-Peperoni: Queso mozzarella, Pepperoni'}

clasica = {'descripcion': '-Clásica: Queso mozzarella, Aceitunas, Jamon, Tomate'}

vegetariana = {'descripcion': '-Vegetariana: Queso mozzarella, Aceitunas, Champiñones, Tomate'}

pollo = {'nombre': 'Pollo',
         'precio': '$1.700',
         'descripcion': 'Rico pollo hecho con amor',
         'categoria': 'Almuerzos',
         'stock': 30,
         'icono': "../../static/img/chicken2.png",
         'imagen': "#modal2"}

menu_arroz = {'nombre': 'Menú de arroz',
              'precio': '$2.500',
              'descripcion': 'Almuerzo de arroz con pollo arvejado.',
              'categoria': 'Almuerzos',
              'stock': 40,
              'icono': "../../static/img/rice.png",
              'imagen': "#modal2"}

jugo = {'nombre': 'Jugo',
        'user': '',
        'precio': '$300',
        'descripcion': 'Jugo en caja sabor durazno.',
        'categoria': 'Snack',
        'stock': 40,
        'icono': "../../static/img/juice.png",
        'imagen': "#modal3"}

info_vendedor = {'nombre': 'Michael Jackson',
                 'tipo_vendedor': 'Vendedor Fijo',
                 'estado': 'Disponible',
                 'formas_de_pago': 'Efectivo',
                 'menus': [pizza, menu_arroz, jugo],
                 'imagen': "../../static/img/AvatarVendedor6.png"}

info_vendedor2 = {'nombre': 'Rata Touille',
                  'tipo_vendedor': 'Vendedor Ambulante',
                  'estado': 'Disponible',
                  'formas_de_pago': 'Tarjeta de credito',
                  'menus': [pizza, pollo, menu_arroz],
                  'imagen': "../../static/img/AvatarVendedor3.png"}


def vendedor_profile(request):
    return render(request, 'app/vendedor_profile.html')


def vendedor_profileAlumno(request):
    return render(request, 'app/vendedor_profileAlumno.html', context=info_vendedor2)


def vendedor_edit(request):
    return render(request, 'app/vendedor_edit.html')


def editar_producto(request):
    return render(request, 'app/editar_producto.html')


def iniciar():
    vendedor_profile()
