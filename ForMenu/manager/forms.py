from django import forms
from django.contrib.auth.models import User
from manager.models import Menu, Horario, Restaurante


class menuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = (
            'nombre',
            'pdf',
        )

class userForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name'
        )



class ajustesForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username'
        )

class emailForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'email',
        )


class restauranteForm(forms.ModelForm):
    class Meta:
        model = Restaurante
        fields = (
            'nombre',
            'telefono',
        )


class direccionForm(forms.ModelForm):
    class Meta:
        model = Restaurante
        fields = (
            'direccion',
            'ciudad',
            'provincia',
            'pais'
        )


class horarioForm(forms.ModelForm):
    class Meta:
        model = Horario
        fields = (
            'lunes',
            'lunesTurno',
            'lunesOpen',
            'lunesClose',
            'lunesOpen2',
            'lunesClose2',
            'martes',
            'martesTurno',
            'martesOpen',
            'martesClose',
            'martesOpen2',
            'martesClose2',
            'miercoles',
            'miercolesTurno',
            'miercolesOpen',
            'miercolesClose',
            'miercolesOpen2',
            'miercolesClose2',
            'jueves',
            'juevesTurno',
            'juevesOpen',
            'juevesClose',
            'juevesOpen2',
            'juevesClose2',
            'viernes',
            'viernesTurno',
            'viernesOpen',
            'viernesClose',
            'viernesOpen2',
            'viernesClose2',
            'sabado',
            'sabadoTurno',
            'sabadoOpen',
            'sabadoClose',
            'sabadoOpen2',
            'sabadoClose2',
            'domingo',
            'domingoTurno',
            'domingoOpen',
            'domingoClose',
            'domingoOpen2',
            'domingoClose2',
        )



