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

        if request.POST['password1'] == request.POST['password2']:
            if User.objects.filter(username=request.POST['username']).exists():
                messages.error(
                    request, f'Nombre de usuario en uso')
            else:
                if form.is_valid():
                    user = form.save()
                    Restaurante.objects.create(user=user, nombre=request.POST['nombre'], telefono=request.POST['telefono'])
                    Horario.objects.create(user=user)
                    messages.success(request, f'Registro realizado')
                    return redirect('login')
                else:
                    messages.error(request, f'Ha avido un error, por favor consulta tu contraseña o tus')
                    form = UserForm()
                
        else:
            messages.error(request, f'Las contraseñas no coinciden')
            form = UserForm()
        
    return render(request, 'public/singup.html')
