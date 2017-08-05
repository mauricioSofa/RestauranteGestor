# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from gestor.models import *
from gestor.forms import *
import datetime
from django.db.models import Sum

# Create your views here.
#
'''
Codigo para la Generacion de tablas con sumatoria
Servicio.objects.values('cliente__nombre').annotate(Sum('costo'))
'''
def tabla_new(request):
    start_date = datetime.date(2016, 11, 8)
    end_date = datetime.date(2016, 11, 8)

    if request.method == "POST":
        form = FiltroForm(request.POST)

        if form.is_valid():
            start_date = form.cleaned_data['inicio_fecha']
            end_date = form.cleaned_data['inicio_fin']
            form = FiltroForm()
            #return render(request, 'gestor/tablaventa.html', {'form': form})
            tablas = Servicio.objects.values('cliente__nombre','cliente__apellidos' , 'cliente__cedula' , 'cliente__dependencia__nombreDependencia', ).annotate(Sum('costo')).filter(fecha__dato_fecha__range = (start_date, end_date))
            contexto = {'tablas':tablas,'form': form}
            return render(request, 'gestor/tablaventa.html',contexto)

    else:
        form = FiltroForm()
        return render(request, 'gestor/tablaventa.html', {'form': form})
'''
    #Renderizado de Tablas
    tablas = Servicio.objects.values('cliente__nombre','cliente__apellidos' , 'cliente__cedula' , 'cliente__dependencia__nombreDependencia', ).annotate(Sum('costo'))
    #tablas = Servicio.objects.all()
    contexto = {'tablas':tablas}
    return render(request, 'gestor/tablaventa.html',contexto)
'''
'''
def post_new(request):
        form = ServicioForm()
        return render(request, 'gestor/index.html', {'form': form})
'''
def venta_new(request):
        if request.method == "POST":
            form = ServicioForm(request.POST)
            if form.is_valid():
                post = form.save()
                form = ServicioForm()
                return render(request, 'gestor/regventa.html', {'form': form})
        else:
            form = ServicioForm()
        return render(request, 'gestor/regventa.html', {'form': form})

def cliente_new(request):
        if request.method == "POST":
            form = PersonForm(request.POST)
            if form.is_valid():
                post = form.save()

                form = PersonForm()
                return render(request, 'gestor/regcliente.html', {'form': form})
        else:
            form = PersonForm()
        return render(request, 'gestor/regcliente.html', {'form': form})

def fecha_new(request):
        if request.method == "POST":
            form = FechaForm(request.POST)
            if form.is_valid():
                post = form
                post.dato_fecha = form.cleaned_data['dato_fecha']
                post = form.save()

                form = FechaForm()
                return render(request, 'gestor/regfecha.html', {'form': form})
        else:
            form = FechaForm()
        return render(request, 'gestor/regfecha.html', {'form': form})
