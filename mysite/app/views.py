# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .forms import LoginForm
from .forms import EditVForm
from .forms import SignupForm
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
        try:
            user = User.objects.get(username=username)
            if UserInfo.objects.get(user=user) != None:
                if user.password == password:
                    user.is_active = 1
                    user.save()
                    usuario = UserInfo.objects.get(user=user)
                    if usuario.tipo == 'fijo' or usuario.tipo == "ambulante":
                        return render(request, 'app/vendedor_profile.html', {'usuario': usuario})
                    else:  # es alumno
                        return render(request, 'app/vendedor_profileAlumno.html', {'usuario': usuario})
                else:
                    return render(request, 'app/login2.html', {'form': form})
        except Exception:
            return render(request, 'app/login2.html', {'form': form})
    else:
        return render(request, 'app/login.html', {'form': form})


def gestion_productos(request):
    return render(request, 'app/gestion_productos.html')


def home(request):
    return render(request, 'app/home.html')


def signup(request):
    form = SignupForm(request.POST)
    page = "app/signup.html"
    clienteNul=User(username="nulo")
    cliente = UserInfo(user=clienteNul)
    #recibe el form
    if (request.method == 'POST' and form.is_valid()):
        username = form.cleaned_data['nombre']
        password = form.cleaned_data['password']
        usertype = form.cleaned_data['usertype']
        email = form.cleaned_data['email']
        hora_inicio = form.cleaned_data['hora_inicio']
        hora_final = form.cleaned_data['hora_final']
        efectivo = form.cleaned_data['efectivo']
        tarjeta_credito = form.cleaned_data['tarjeta_credito']
        tarjeta_debito = form.cleaned_data['tarjeta_debito']
        tarjeta_junaeb = form.cleaned_data['tarjeta_junaeb']

        if (usertype == "3"):  # es un cliente
            user = User(username=username, email=email, password=password)
            user.is_active = 1
            user.save()
            cliente = Alumno(user=User.objects.get(username=username), tipo='alumno')
            cliente.save()
            page = 'app/index.html'
            return render(request, 'app/index.html')

        elif (usertype == "1"): # es un vendedor fijo

            user = User(username=username, email=email, password=password)
            user.is_active = 1
            user.save()
            cliente = VendedorFijo(user=User.objects.get(username=username), tipo='fijo',
                                             apertura=hora_inicio, cierre=hora_final,
                                             tarj_cred=tarjeta_credito, tarj_deb=tarjeta_debito,
                                             tarj_junaeb=tarjeta_junaeb)
            cliente.save()
            return render(request,'app/vendedor_profile.html')
        elif (usertype == "2"): # es un vendedor ambulante

            user = User(username=username, email=email, password=password)
            user.is_active = 1
            user.save()
            cliente = VendedorAmbulante(user=User.objects.get(username=username), tipo='ambulante',
                                                 tarj_cred=tarjeta_credito, tarj_deb=tarjeta_debito,
                                                 tarj_junaeb=tarjeta_junaeb)
            cliente.save()
            page = 'app/vendedor_profile.html'
            return render(request,'app/vendedor_profile.html')
    return render(request,'app/signup.html',{'form':form})



# informacion de test
pizza_clasica = {'nombre': 'Pizza Clasica',
                 'user': 'Rata Touille',
                 'precio': '$1.300',
                 'descripcion': 'Deliciosa pizza con: Queso mozzarella, Aceitunas, Jamon, Tomate',
                 'categoria': 'Almuerzos',
                 'stock': 20,
                 'icono': "../../static/img/pizza.png",
                 'imagen': "#modal1"}

pizza_peperoni = {'nombre': 'Pizza Pepperoni',
                  'user': 'michaeljackson',
                  'precio': '$1.300',
                  'descripcion': 'Deliciosa pizza con: Queso mozzarella, Pepperoni',
                  'categoria': 'Almuerzos',
                  'stock': 20,
                  'icono': "../../static/img/pizza.png",
                  'imagen': "#modal1"}

pizza_vegetariana = {'nombre': 'Pizza Vegetariana',
                     'user': 'michaeljackson',
                     'precio': '$1.300',
                     'descripcion': 'Deliciosa pizza con: Queso mozzarella, Aceitunas, Champiñones, Tomate',
                     'categoria': 'Almuerzos',
                     'stock': 20,
                     'icono': "../../static/img/pizza.png",
                     'imagen': "#modal1"}

pollo = {'nombre': 'Pollo',
         'user': 'Rata Touille',
         'precio': '$1.700',
         'descripcion': 'Rico pollo hecho con amor',
         'categoria': 'Almuerzos',
         'stock': 30,
         'icono': "../../static/img/chicken2.png",
         'imagen': "#modal2"}

menu_arroz = {'nombre': 'Menú de arroz',
              'user': 'Rata Touille',
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

def get_info(producto):
    info = {
        'nombre' : producto.nombre,
        'user' : producto.user,
        'precio' : producto.precio,
        'decripcion' : producto.descripcion,
        'categoria' : producto.categoria,
        'stock' : producto.stock,
        'icono' : producto.imagen,
        'imagen' : producto.img_referencia,
    }
    return info

def get_menus(user):
    productos = []
    for i in Productos.objects.filter(user = user):
        productos.append(get_info(i))
    return productos


def vendedor_profile(request):
    return render(request, 'app/vendedor_profile.html')


def vendedor_profileAlumno(request):
    usuario = 'ratatouille'
    clase_user = User.objects.get(username=usuario)
    clase_info = UserInfo.objects.get(user_id=clase_user.id)
    clase_vendedor = Vendedor.objects.get(userinfo_ptr_id=clase_user.id)
    tipo = 'Vendedor Ambulante'
    if 'fijo' in  clase_info.tipo:
        tipo = 'Vendedor Fijo'
    formas_de_pago = []
    if clase_vendedor.efectivo == 1:
        formas_de_pago.append('Efectivo')
    if clase_vendedor.tarj_cred == 1:
        formas_de_pago.append('Tarjeta de Credito')
    if clase_vendedor.tarj_deb == 1:
        formas_de_pago.append('Tarjeta de Debito')
    if clase_vendedor.tarj_junaeb == 1:
        formas_de_pago.append('Tarjeta Junaeb')
    estado = 'Inactivo'
    if clase_user.is_active:
        estado = 'Activo'
    info_vendedor = {
        'nombre' : clase_vendedor.nombre_visible,
        'tipo_vendedor' : tipo,
        'estado' : estado,
        'formas_de_pago' : formas_de_pago,
        'menus' : get_menus(usuario),
        'imagen' : clase_vendedor.archivo_foto_perfil
    }
    return render(request, 'app/vendedor_profileAlumno.html', context=info_vendedor)

def vendedor_edit(request):
    form = EditVForm(request.POST)
    # formulario lleno, edicion de datos
    usuario = User.objects.get(is_active=1)
    if request.method == 'POST' and form.is_valid():
        # obtengo mail y pass
        nombre = form.cleaned_data['your_name']
        foto = form.cleaned_data['file']
        # si alguno es != de None lo actualizo
        if nombre != None:
            usuario.first_name = nombre
            usuario.save()
        if foto != None:
            usuario = Vendedor.objects.get(user=usuario)
            usuario.archivo_foto_perfil = foto
            usuario.save()
        return render(request, 'app/vendedor_profile.html', {'usuario': usuario})
    else:
        form = EditVForm()
        return render(request, 'app/vendedor_edit.html', {'form': form, 'usuario': usuario})



def editar_producto(request, value=None):
    return render(request, 'app/editar_producto.html')


def iniciar():
    vendedor_profile()
