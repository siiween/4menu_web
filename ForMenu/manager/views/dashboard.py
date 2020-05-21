# django
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.hashers import check_password

# models
from manager.models import Restaurante, Horario, Menu
# forms
from manager.forms import menuForm, emailForm, restauranteForm, direccionForm, horarioForm, userForm, ajustesForm
# utils
import qrcode
from unidecode import unidecode


@login_required
def dashboard(request):
    restaurante = Restaurante.objects.get(user=request.user)
    horario = Horario.objects.get(user=request.user)
    menus = Menu.objects.filter(user=request.user)
    context = {
        'restaurante': restaurante,
        'horario': horario,
        'menus': menus,
    }

    return render(request, 'manager/dashboard.html', context)


@login_required
def crearMenu(request):
    if request.method == 'POST':
        form = menuForm(request.POST, request.FILES)
        if form.is_valid():
            menu = form.save(commit=False)
            menu.user = request.user
            # generamos el slugname
            menu.slug_name = unidecode(
                request.POST['nombre']).lower().replace(' ', '_')
            menu.save()
            # generamos el QR
            img = qrcode.make('https://www.4menu.es/media/' + str(menu.pdf))
            img.save(settings.MEDIA_ROOT + '/QR/' +
                     menu.user.username + '_' + menu.slug_name + '.png')
            menu.qr = 'QR/' + menu.user.username + '_' + menu.slug_name + '.png'
            menu.save()
            messages.success(
                request, f'¡Enhorabuena! Tu menú ha sido creado correctamente')
        else:
            messages.error(
                request, f'Ha habido un error, prueba de nuevo')

    return redirect('dashboard-manager')


@login_required
def eliminarMenu(request, id):
    menu = Menu.objects.get(id=id)

    if request.user == menu.user:
        if menu.delete():
            messages.success(request, f'Menú eliminado correctamente')
        else:
            messages.error(
                request, f'Ha habido un error, prueba de nuevo')
    else:
        messages.error(request, f'No puedes eliminar menús que no son tuyos')

    return redirect('dashboard-manager')


@login_required
def modificarImagen(request):
    if request.method == 'POST':
        restaurante = Restaurante.objects.get(user=request.user)
        restaurante.imagen = request.FILES['imagen']
        restaurante.save()
        messages.success(request, f'Imagen modificada correctamente')
    return redirect('dashboard-manager')


@login_required
def modificarDatosPublicos(request):
    if request.method == 'POST':
        restaurante = Restaurante.objects.get(user=request.user)

        e_form = emailForm(request.POST, instance=request.user)
        r_form = restauranteForm(request.POST, instance=restaurante)

        if e_form.is_valid() and r_form.is_valid():
            e_form.save()
            r_form.save()
            messages.success(
                request, f'¡Tus datos públicos han sido actualizado!')
        else:
            messages.error(
                request, f'Ha habido un error, prueba de nuevo')
    return redirect('dashboard-manager')



@login_required
def modificarDireccion(request):
    if request.method == 'POST':
        restaurante = Restaurante.objects.get(user=request.user)
        form = direccionForm(request.POST, instance=restaurante)
        if form.is_valid():
            form.save()
            messages.success(
                request, f'¡Tu dirección ha sido modificada!')
        else:
            messages.error(
                request, f'Ha habido un error, prueba de nuevo')
    return redirect('dashboard-manager')


@login_required
def modificarHorario(request):
    if request.method == 'POST':
        horario = Horario.objects.get(user=request.user)

        form = horarioForm(request.POST, instance=horario)

        if form.is_valid():
            form.save()
            messages.success(request, f'¡Tu horario ha sido modificado!')
        else:
            messages.error(
                request, f'Ha habido un error, prueba de nuevo')
    return redirect('dashboard-manager')


@login_required
def completarPerfil(request):
    if request.method == 'POST':
        horario = Horario.objects.get(user=request.user)
        restaurante = Restaurante.objects.get(user=request.user)

        u_form = userForm(request.POST, instance = request.user)
        h_form = horarioForm(request.POST, instance=horario)
        r_form = direccionForm(request.POST, instance=restaurante)

        if h_form.is_valid() and r_form.is_valid() and u_form.is_valid():
            h_form.save()
            r_form.save()
            u_form.save()
            restaurante.is_complete = True
            restaurante.save()

            messages.success(request, f'¡Tu cuenta ha sido completada!')
        else:
            messages.error(
                request, f'No se ha podido completar tu cuenta')
    return redirect('dashboard-manager')





@login_required
def ajustes(request):
    if request.method == 'POST':
        form = ajustesForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, f'¡Tus datos han sido actualizados!')
        else:
            messages.error(
                request, f'Ha habido un error, prueba de nuevo')
    return redirect('dashboard-manager')


@login_required
def password(request):
    if request.method == 'POST':
        if check_password(request.POST['passwordOld'], request.user.password):
            if request.POST['password'] == request.POST['password2']:
                request.user.set_password(request.POST['password'])
                request.user.save()
                messages.success(
                    request, f'Tu contraseña ha sido modificada, por favor vuelve a iniciar sesión')
            else:
                messages.error(
                    request, f'Las contraseñas no coincides')
        else:
            messages.error(
                    request, f'La contraseña anterior es incorrecta')
    return redirect('dashboard-manager')
