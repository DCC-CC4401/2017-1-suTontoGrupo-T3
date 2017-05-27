# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .forms import LoginForm


def index(request):
    return render(request, 'app/index.html')


def login(request):
    form = LoginForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        # procesaaar
        return render(request, 'app/vendedor_profile.html', )
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
