# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


def index(request):
    return render(request, 'app/index.html')


def login(request):
    return render(request, 'app/login.html')


def gestion_productos(request):
    return render(request, 'app/gestion_productos.html')


def home(request):
    return render(request, 'app/home.html')


def signup(request):
    return render(request, 'app/signup.html')


def vendedor_profile(request):
    return render(request, 'app/vendedor_profile.html')


def vendedor_profileAlumno(request):
    return render(request, 'app/vendedor_profileAlumno.html')


def vendedor_edit(request):
    return render(request, 'app/vendedor_edit.html')


def editar_producto(request):
    return render(request, 'app/editar_producto.html')
