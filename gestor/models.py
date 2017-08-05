# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.contrib import admin
from django.db import models

# Create your models here.
class Dependencia(models.Model):
    nombreDependencia = models.CharField(max_length = 30, default= "Pool de Ambulancia")

    def __str__(self):
            return str(self.nombreDependencia)

class Person(models.Model):
    nombre = models.CharField(max_length = 30)
    apellidos = models.CharField(max_length = 30)
    cedula = models.IntegerField()
    dependencia = models.ForeignKey(Dependencia,)

    def __str__(self):
            return str(self.nombre + " " + self.apellidos)
class Fecha(models.Model):
    dato_fecha = models.DateField(primary_key=True,default=timezone.now)
    def __str__(self):
            return str(self.dato_fecha)

class Servicio(models.Model):
    cliente = models.ForeignKey(Person)
    fecha = models.ForeignKey(Fecha)
    costo = models.IntegerField(default=0)
    def __str__(self):
            return str(self.cliente )+ " $" + str(self.costo) + " - " + str(self.fecha)

admin.site.register(Dependencia)
admin.site.register(Person)
admin.site.register(Fecha)
admin.site.register(Servicio)
