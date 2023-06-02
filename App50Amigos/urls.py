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
from django.conf import settings

app_name = 'App50Amigos'

urlpatterns = [
   path('', views.index, name='index'),
   path('administrador/', views.panelAdmin, name='panel_admin'),
   path('usuario/', views.panelUser, name='panel_user'),
   path('registro/', views.registro, name = 'registro')
]
