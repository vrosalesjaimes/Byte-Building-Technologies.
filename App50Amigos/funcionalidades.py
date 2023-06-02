from django.shortcuts import render, redirect
from .models import *

def asignacion_mesa(request):
    if request.method == 'POST':
        num_mesa = request.POST.get('NumMesa')
        ubicacion = request.POST.get('ubicacion')
        id_encargado = request.POST.get('id_Encargado')
        id_tableta = request.POST.get('id_tableta')

        print(num_mesa, ubicacion, id_tableta, id_encargado)
        return redirect('App50Amigos:bienvenida')

