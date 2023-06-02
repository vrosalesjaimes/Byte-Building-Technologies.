"""Proyecto50Amigos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from .funcionalidades import  *
from django.conf import settings

app_name = 'App50Amigos'

urlpatterns = [
   path('', views.index, name='index'),
   path('administrador/', views.panelAdmin, name='panel_admin'),
   path('usuario/<int:id_tableta>/<int:num_mesa>/<str:ubicacion>/<int:id_order>/',
        views.panelUser, name='panel_user'),
   path('carrito/', views.carrito, name='carrito'),
   path('votación', views.votacion, name='votacion'),
   path('registro/', views.registro, name = 'registro'),
   path('bienvenida/<int:id_tableta>/<int:num_mesa>/<str:ubicacion>/', views.fondo, name='bienvenida')
   #path('asignacion_mesa/<parametros>')
]
