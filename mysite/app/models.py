# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.


class UserInfo(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                primary_key=True,
                                )
    tipo = models.CharField(max_length=10)

class Alumno(UserInfo):
    pass

class Vendedor(UserInfo):
    nombre_visible = models.CharField(max_length=50)
    archivo_foto_perfil = models.ImageField(upload_to='app/static/')
    efectivo = models.BooleanField()
    tarj_cred = models.BooleanField()
    tarj_deb = models.BooleanField()
    tarj_junaeb = models.BooleanField()


class VendedorAmbulante(Vendedor):
    check_in = models.BooleanField



class VendedorFijo(Vendedor):
    apertura = models.TimeField
    cierre = models.TimeField



class Favoritos(models.Model):
    alumno = models.OneToOneField(Alumno,
                                  on_delete=models.CASCADE,
                                  primary_key=False,
                                  )
    favorito = models.OneToOneField(Vendedor,
                                    on_delete=models.CASCADE,
                                    primary_key=False
                                    )


class Productos(models.Model):
    nombre = models.CharField(max_length=50)
    user = models.OneToOneField(Vendedor,
                                on_delete=models.CASCADE,
                                primary_key=False,
                                )
    precio = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50)
    stock = models.IntegerField
    imagen = models.ImageField(upload_to='app/static/')
    img_referencia = models.ImageField(upload_to='app/static/')
