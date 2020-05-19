# django
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# models



def inicio(request):
    if request.user.is_authenticated:
        return redirect('dashboard-manager')
    return render(request, 'public/inicio.html')

def buscador(request):
    if request.user.is_authenticated:
            return redirect('dashboard-manager')
    nombre = request.GET.get('n')
    ciudad = request.GET.get('c')

    context = {
        'ciudad': ciudad,
        'nombre':nombre,
    }

    return render(request, 'public/buscador.html', context)


def local(request):
    if request.user.is_authenticated:
            return redirect('dashboard-manager')

    return render(request, 'public/local.html')
