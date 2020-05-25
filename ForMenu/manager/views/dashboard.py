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
    # pantalla principal donde se muestra todo lo que puede hacer un
    # cliente registrado
    if request.user.is_superuser:
        return redirect('/admin')

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
    # función que permite crear menús y generar el QR único que estos tendrás
    if request.method == 'POST':
        form = menuForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                menu = form.save(commit=False)
                menu.user = request.user
                menu.save()
                # generamos el QR una vez el pdf esté guardado para que no de errores
                img = qrcode.make('https://www.4menu.es/descargar/' + str(menu.id))
                img.save(settings.MEDIA_ROOT + '/QR/' + menu.user.username + '_' + str(menu.id) + '.png')
                # lo asignamos al menú que acabamos de crear antes
                menu.qr = 'QR/' + menu.user.username + '_' + str(menu.id) + '.png'
                menu.save()
                messages.success(request, f'¡Enhorabuena JOSE! Tu menú ha sido creado correctamente')
            except:
                # no se ha logrado crear el qr por lo que eliminamos todo para que no de fallo
                menu.delete()
                messages.error(request, f'Ha habido un error, prueba de nuevo')
        else:
            messages.error(request, f'Ha habido un error, prueba de nuevo')
    return redirect('dashboard-manager')





@login_required
def modificarMenu(request, id):
    # función que nos permite cambiar el archivo y nombre de un Menú
    menu = Menu.objects.get(id=id)

    if request.user == menu.user:
        if request.method == 'POST':
            form = menuForm(request.POST, request.FILES, instance=menu)
            if form.is_valid():
                menu = form.save()
                menu.save()
                messages.success(request, f'¡Enhorabuena! Tu menú ha sido modificado correctamente')
        else:
            messages.error(request, f'Ha habido un error, prueba de nuevo')
    else:
        messages.error(request, f'No puedes modificar menús que no son tuyos')

    return redirect('dashboard-manager')





@login_required
def eliminarMenu(request, id):
    # función que nos permite eliminar un menú 
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
    # función que modifica la imagen de perfil de un restaurante
    if request.method == 'POST':
        restaurante = Restaurante.objects.get(user=request.user)
        restaurante.imagen = request.FILES['imagen']
        restaurante.save()
        messages.success(request, f'Imagen modificada correctamente')
    return redirect('dashboard-manager')





@login_required
def modificarDatosPublicos(request):
    # función que nos permite modificar los datos publicos
    # de un restaurante
    if request.method == 'POST':
        restaurante = Restaurante.objects.get(user=request.user)

        e_form = emailForm(request.POST, instance=request.user)
        r_form = restauranteForm(request.POST, instance=restaurante)

        if e_form.is_valid() and r_form.is_valid():
            e_form.save()
            r_form.save()
            messages.success(
                request, f'¡Tus datos públicos han sido actualizados!')
        else:
            messages.error(
                request, f'Ha habido un error, prueba de nuevo')
    return redirect('dashboard-manager')





@login_required
def modificarDireccion(request):
    # función que nos permite modificar la dirección de un restaurante
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
    # función que nos permite modificar el horario de un restaurante
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
    # función que nos ayuda a que cuando un restaurante se acaba de
    # registrar termine de registrar y rellenar los datos de su perfil
    # para que no hallan errores ni campos vacios
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
    # función que nos permite modificar los datos personales de un restaurante
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
    # función que nos permite modificar la contraseña de un restaurante
    if request.method == 'POST':
        if check_password(request.POST['passwordOld'], request.user.password):
            if request.POST['password'] == request.POST['password2']:
                request.user.set_password(request.POST['password'])
                request.user.save()
                messages.success(
                    request, f'Tu contraseña ha sido modificada, por favor vuelve a iniciar sesión')
            else:
                messages.error(
                    request, f'Las contraseñas no coinciden')
        else:
            messages.error(
                    request, f'La contraseña anterior es incorrecta')
    return redirect('dashboard-manager')


