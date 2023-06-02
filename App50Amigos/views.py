from django.shortcuts import render, HttpResponse, redirect
from urllib.parse import urlencode
from .models import *
from .forms import *
from django.http import JsonResponse
from django.urls import reverse

from django.contrib import messages
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import *
from .funcionalidades import *
import uuid
# Create your views here.


def index(request):

    if request.method == 'POST':
        num_mesa = request.POST.get('NumMesa')
        ubicacion = request.POST.get('ubicacion')
        id_encargado = request.POST.get('id_Encargado')
        id_tableta = request.POST.get('id_tableta')

        return redirect('App50Amigos:bienvenida', id_tableta, num_mesa, ubicacion)

    return render(request,'index.html')


def fondo(request, id_tableta, num_mesa, ubicacion):

    if request.method == 'POST':
        id_order = int(uuid.uuid4().int)
        print(id_order)
        return redirect('App50Amigos:panel_user', id_tableta, num_mesa, ubicacion, id_order)

    return render(request, 'fondo.html')

def panelAdmin(request):
    entradas = Platillo.objects.filter(categoria='Entrada')
    platos_fuerte = Platillo.objects.filter(categoria='Plato Fuerte')
    bebidas = Platillo.objects.filter(categoria='Bebida')
    postres = Platillo.objects.filter(categoria='Postre')
    helados = Platillo.objects.filter(categoria='Helado')
    return render(request, 'panels/panel_admin.html', {'entradas': entradas,
                                                       'platos_fuertes': platos_fuerte,
                                                       'bebidas': bebidas,
                                                       'postres': postres,
                                                       'helados': helados})

def panelUser(request, id_tableta, num_mesa, ubicacion, id_order):
    entradas = Platillo.objects.filter(categoria='Entrada')
    platos_fuerte= Platillo.objects.filter(categoria='Plato Fuerte')
    bebidas = Platillo.objects.filter(categoria='Bebida')
    postres = Platillo.objects.filter(categoria='Postre')
    return render(request, 'panels/panel_user.html',  {'entradas': entradas,
                                                       'platos_fuertes': platos_fuerte,
                                                       'bebidas': bebidas,
                                                       'postres': postres,
                                                       'num_mesa': num_mesa,
                                                       'ubicacion': ubicacion})

def carrito(request):
    return render(request, 'panels/pedido.html')

def votacion(request):
    return render(request, 'panels/votacion.html')

def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == "POST":
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            usuario = formulario.save()
            usuario.save()
            user = authenticate(username = formulario.cleaned_data["username"], password = formulario.cleaned_data["password1"])
            login(request,user)
            messages.success(request, "Registro exitoso, inicia sesión")
            return redirect(to="App50Amigos:P1")
        data["form"] = formulario

    return render(request, 'registration/registration.html', data)