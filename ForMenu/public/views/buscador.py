# django
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
#utils
from django.db.models import Q
# models
from manager.models import Restaurante, Menu, Horario
from datetime import date

def terminos(request):
    return render(request, 'public/terminos.html')




def inicio(request):
    if request.user.is_authenticated:
        return redirect('dashboard-manager')
    return render(request, 'public/inicio.html')




def buscador(request):
    if request.user.is_authenticated:
            return redirect('dashboard-manager')
    nombre = request.GET.get('n')
    ciudad = request.GET.get('c')

    if not ciudad and not nombre:
        restaurantes = []
        menus = []
    else:
        if not ciudad and nombre:
            qset = (
                Q(nombre__icontains=nombre) |
                Q(user__username__icontains=nombre)
            )
        if ciudad and not nombre:
            qset = (
                Q(ciudad__icontains=ciudad) |
                Q(provincia__icontains=ciudad)
            )
        else:
            qset = (
                (Q(nombre__icontains=nombre) |
                Q(user__username__icontains=nombre)) &
                (Q(ciudad__icontains=ciudad) |
                Q(provincia__icontains=ciudad))
            )
        restaurantes = Restaurante.objects.filter(qset).distinct().order_by('created')
        menus = []
        for restaurante in restaurantes:
            menus += Menu.objects.filter(user = restaurante.user)

    context = {
        'ciudad': ciudad,
        'nombre': nombre,
        'restaurantes': restaurantes,
        'menus': menus
    }

    return render(request, 'public/buscador.html', context)





def local(request, username):
    if request.user.is_authenticated:
            return redirect('dashboard-manager')

    user = User.objects.get(username = username)
    restaurante = Restaurante.objects.get(user=user)
    horario = Horario.objects.get(user=user)
    menus = Menu.objects.filter(user=user)
    
    context = {
        'restaurante': restaurante,
        'horario': horario,
        'menus': menus,
        'usuario': user,
    }
    return render(request, 'public/local.html', context)




def descargar(request, id):
    pdf = Menu.objects.get(id = id)
    return redirect(pdf.pdf.url)
