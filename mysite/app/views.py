# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .forms import LoginForm
from .forms import EditVForm
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

        if UserInfo.objects.get(user=User.objects.get(username=username)) != None:
            #auth.login(request, username)
            usuario = UserInfo.objects.get(user=User.objects.get(username=username))
            if usuario.tipo == 'fijo' or usuario.tipo == "ambulante":
                return render(request, 'app/vendedor_profile.html', {'usuario': usuario})
            else: # es alumno
                return render(request, 'app/vendedor_profileAlumno.html', {'usuario': usuario})
    else:
        return render(request, 'app/login.html', {'form': form})


def gestion_productos(request):
    return render(request, 'app/gestion_productos.html')


def home(request):
    return render(request, 'app/home.html')


def signup(request):
    form = LoginForm(request.POST)
    if (request.method == 'POST' and form.is_valid()):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        usertype = form.cleaned_data['usertype']
        email = form.cleaned_data['email']
        hora_inicio = form.cleaned_data['hora_inicio']
        hora_final = form.cleaned_data['hora_final']
        efectivo = form.cleaned_data['efectivo']
        tarjeta_credito = form.cleaned_data['tarjeta_credito']
        tarjeta_debito = form.cleaned_data['tarjeta_debito']
        tarjeta_junaeb = form.cleaned_data['tarjeta_junaeb']

        if (usertype == 3): # es un cliente
            user = User(username=username, email=email, password=password)
            user.save()
            cliente = Alumno(user=User.objects.get(username=username), tipo='alumno')
            cliente.save()
        elif (usertype == 1): # es un vendedor fijo
            user = User(username=username, email=email, password=password)
            user.save()
            cliente_vend_fijo = VendedorFijo(user=User.objects.get(username=username), tipo='fijo')
            cliente_vend_fijo.save()
        elif (usertype == 2): # es un vendedor ambulante
            user = User(username=username, email=email, password=password)
            user.save()
            cliente_vend_amb = VendedorAmbulante(user=User.objects.get(username=username), tipo='ambulante')
            cliente_vend_amb.save()

    return render(request, 'app/signup.html')

# informacion de test
pizza_clasica = {'nombre': 'Pizza Clasica',
         'user' : 'Rata Touille',
         'precio': '$1.300',
         'descripcion': 'Deliciosa pizza con: Queso mozzarella, Aceitunas, Jamon, Tomate',
         'categoria': 'Almuerzos',
         'stock': 20,
         'icono': "../../static/img/pizza.png",
         'imagen': "#modal1"}

pizza_peperoni = {'nombre': 'Pizza Pepperoni',
         'user' : 'Michael Jackson',
         'precio': '$1.300',
         'descripcion': 'Deliciosa pizza con: Queso mozzarella, Pepperoni',
         'categoria': 'Almuerzos',
         'stock': 20,
         'icono': "../../static/img/pizza.png",
         'imagen': "#modal1"}

pizza_vegetariana = {'nombre': 'Pizza Vegetariana',
         'user' : 'Michael Jackson',
         'precio': '$1.300',
         'descripcion': 'Deliciosa pizza con: Queso mozzarella, Aceitunas, Champiñones, Tomate',
         'categoria': 'Almuerzos',
         'stock': 20,
         'icono': "../../static/img/pizza.png",
         'imagen': "#modal1"}

pollo = {'nombre': 'Pollo',
         'user' : 'Rata Touille',
         'precio': '$1.700',
         'descripcion': 'Rico pollo hecho con amor',
         'categoria': 'Almuerzos',
         'stock': 30,
         'icono': "../../static/img/chicken2.png",
         'imagen': "#modal2"}

menu_arroz = {'nombre': 'Menú de arroz',
              'user' : 'Rata Touille',
              'precio': '$2.500',
              'descripcion': 'Almuerzo de arroz con pollo arvejado.',
              'categoria': 'Almuerzos',
              'stock': 40,
              'icono': "../../static/img/rice.png",
              'imagen': "#modal2"}

jugo = {'nombre': 'Jugo',
        'user': 'Rata Touille',
        'precio': '$300',
        'descripcion': 'Jugo en caja sabor durazno.',
        'categoria': 'Snack',
        'stock': 40,
        'icono': "../../static/img/juice.png",
        'imagen': "#modal3"}

menus = [pizza_clasica, pizza_peperoni, pizza_vegetariana, pollo, menu_arroz, jugo]

def get_menus(nombre):
    menus_usuario = []
    for comida in menus:
        if comida['user'] == nombre:
            menus_usuario.append(comida)
    return menus_usuario


info_vendedor = {'nombre': 'Michael Jackson',
                 'tipo_vendedor': 'Vendedor Fijo',
                 'estado': 'Disponible',
                 'formas_de_pago': 'Efectivo',
                 'menus': get_menus('Michael Jackson'),
                 'imagen': "../../static/img/AvatarVendedor6.png"}

info_vendedor2 = {'nombre': 'Rata Touille',
                  'tipo_vendedor': 'Vendedor Ambulante',
                  'estado': 'Disponible',
                  'formas_de_pago': 'Tarjeta de credito',
                  'menus': get_menus('Rata Touille'),
                  'imagen': "../../static/img/AvatarVendedor3.png"}

def vendedor_profile(request):
    return render(request, 'app/vendedor_profile.html')



def vendedor_profileAlumno(request):
    return render(request, 'app/vendedor_profileAlumno.html', context=info_vendedor2)


def vendedor_edit(request):
    form = EditVForm(request.POST)
    # formulario lleno, edicion de datos
    if request.method == 'POST' and form.is_valid():
        # obtengo mail y pass
        nombre = form.cleaned_data['your_name']
        foto = form.cleaned_data['file']
        # si alguno es != de None lo actualizo
        if (nombre != None):
            usuario= auth.get_user(request)
            usuario.username= nombre
            usuario.save()
        if(foto != None):
            usuario=auth.get_user(request)
        return render(request, 'app/vendedor_profile.html', {'usuario': usuario})
    else:
        form= EditVForm()
        return render(request,'app/vendedor_edit.html',{'form': form})




def editar_producto(request):
    return render(request, 'app/editar_producto.html')


def iniciar():
    vendedor_profile()
