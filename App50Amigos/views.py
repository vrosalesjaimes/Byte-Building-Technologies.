from django.shortcuts import render, HttpResponse, redirect
from .models import *
from .forms import *

from django.contrib import messages
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import authenticate, login as auth_login, logout
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):   
    return render(request,'index.html')


def panelAdmin(request):
    return render(request, 'panels/panel_admin.html')

def panelUser(request):
    return render(request, 'panels/panel_user.html')



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

class RegistrationView(CreateView):
    template_name = 'registration/register.html'
    form_class = RegistrationForm

    def get_context_data(self, *args, **kwargs):
        context = super(RegistrationView, self).get_context_data(*args, **kwargs)
        context['next'] = self.request.GET.get('next')
        return context

    def get_success_url(self):
        next_url = self.request.POST.get('next')
        success_url = reverse('login')
        if next_url:
            success_url += '?next={}'.format(next_url)

        return success_url
    

      