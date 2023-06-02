from django.shortcuts import render, HttpResponse, redirect
from .models import *
from .forms import *

from django.contrib import messages
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import *
from .funcionalidades import *
# Create your views here.


def index(request):
    if request.method == 'POST':
        num_mesa = request.POST.get('NumMesa')
        ubicacion = request.POST.get('ubicacion')
        id_encargado = request.POST.get('id_Encargado')
        id_tableta = request.POST.get('id_tableta')
        print(num_mesa, ubicacion, id_tableta, id_encargado)
        return redirect('App50Amigos:bienvenida')

    return render(request,'index.html')

def fondo(request):
    return render(request, 'fondo.html')

def panelAdmin(request):
    entradas = Platillo.objects.filter(categoria='Entrada')
    platos_fuerte = Platillo.objects.filter(categoria='Plato Fuerte')
    bebidas = Platillo.objects.filter(categoria='Bebida')
    postre = Platillo.objects.filter(categoria='Postre')
    helado = Platillo.objects.filter(categoria='Helado')
    return render(request, 'panels/panel_admin.html', {'entradas': entradas,
                                                       'platos_fuertes': platos_fuerte,
                                                       'bebidas': bebidas,
                                                       'postre': postre,
                                                       'helado': helado})

def panelUser(request):
    entradas = Platillo.objects.filter(categoria='Entrada')
    platos_fuerte= Platillo.objects.filter(categoria='Plato Fuerte')
    bebidas = Platillo.objects.filter(categoria='Bebida')
    postre = Platillo.objects.filter(categoria='Postre')
    return render(request, 'panels/panel_user.html',  {'entradas': entradas,
                                                       'platos_fuertes': platos_fuerte,
                                                       'bebidas': bebidas,
                                                       'postre': postre})

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