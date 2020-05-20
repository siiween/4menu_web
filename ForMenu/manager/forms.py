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
            'username',
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
            'lunesOpen',
            'lunesClose',
            'martes',
            'martesOpen',
            'martesClose',
            'miercoles',
            'miercolesOpen',
            'miercolesClose',
            'jueves',
            'juevesOpen',
            'juevesClose',
            'viernes',
            'viernesOpen',
            'viernesClose',
            'sabado',
            'sabadoOpen',
            'sabadoClose',
            'domingo',
            'domingoOpen',
            'domingoClose',
        )



