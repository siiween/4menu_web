# django
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# models
from manager.models import Restaurante, Horario
from public.forms import UserForm





def singup(request):
    # función que nos permite registrar correctamente un restaurante
    # comprobamos existencia de usuarios y seguridad de contraseña
    if request.user.is_authenticated:
        return redirect('dashboard-manager')

    if request.method == 'POST':
        form = UserForm(request.POST)
        nombre = request.POST['nombre']
        telefono = request.POST['telefono']

        if form.is_valid():
            user = form.save()
            Restaurante.objects.create(user=user, nombre=nombre, telefono=telefono)
            Horario.objects.create(user=user)
            messages.success(request, f'Registro realizado')
            return redirect('login')
    else:
        form = UserForm()
        nombre = ''
        telefono = ''

    context = {
        'form': form,
        'nombre' : nombre,
        'telefono': telefono,
    }
        #else:
            #messages.error(request, f'Las contraseñas no coinciden')
            #form = UserForm()
        
    return render(request, 'public/singup.html', context)
