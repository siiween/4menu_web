# django
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# models
from manager.models import Restaurante, Horario
from public.forms import UserForm


def singup(request):
    if request.user.is_authenticated:
        return redirect('dashboard-manager')

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()

            Restaurante.objects.create(user=user, nombre=request.POST['nombre'], telefono=request.POST['telefono'])
            Horario.objects.create(user=user)

            messages.error(request, f'Registro realizado')
            return redirect('login')
        else:
            form = UserForm()
            messages.error(request, f'Ha habido un error en tus datos de usuario')
            
    return render(request, 'public/singup.html')
