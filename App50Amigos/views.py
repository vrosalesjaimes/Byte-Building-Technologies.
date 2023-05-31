from django.shortcuts import render, HttpResponse
from .forms import FormAdmin


# Create your views here.
def index(request):
    login_form = FormAdmin()
    print(login_form)
    return render(request, 'index.html', {'login_form': login_form})

