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
            if usuario.tipo =='vendedor':
                return render(request, 'app/vendedor_profile.html',{'usuario':usuario})
            else :
                return render(request,'app/vendedor_profileAlumno.html',{'usuario':usuario})
    else:
        form = LoginForm()

    return render(request, 'app/login.html', {'form': form})


def gestion_productos(request):
    return render(request, 'app/gestion_productos.html')


def home(request):
    return render(request, 'app/home.html')


def signup(request):
    return render(request, 'app/signup.html')


def vendedor_profile(request):
    return render(request, 'app/vendedor_profile.html', )


def vendedor_profileAlumno(request):
    return render(request, 'app/vendedor_profileAlumno.html')


def vendedor_edit(request):
    return render(request, 'app/vendedor_edit.html')


def editar_producto(request):
    return render(request, 'app/editar_producto.html')


def iniciar():
    vendedor_profile()
