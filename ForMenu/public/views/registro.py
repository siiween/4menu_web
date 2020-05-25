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

        if request.POST['password1'] == request.POST['password2']:
            if User.objects.filter(username=request.POST['username']).exists():
                messages.error(
                    request, f'Nombre de usuario en uso')
            else:
                if form.is_valid():
                    user = form.save()
                    # comprobamos si se crea el restaurante y el horario para el usuario y si no es así
                    # lo eliminamos para evitar fallos
                    try:
                        Restaurante.objects.create(user=user, nombre=request.POST['nombre'], telefono=request.POST['telefono'])
                        Horario.objects.create(user=user)
                        messages.success(request, f'Registro realizado')
                        return redirect('login')
                    except:
                        user.delete()
                        messages.error(request, f'Ha habido un error, por favor intentelo de nuevo')
                        form = UserForm()
                else:
                    messages.error(request, f'Por favor modifica tu contraseña, ya que no es segura')
                    form = UserForm()
                
        else:
            messages.error(request, f'Las contraseñas no coinciden')
            form = UserForm()
        
    return render(request, 'public/singup.html')
