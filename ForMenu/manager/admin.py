from django.contrib import admin
from manager.models import *
# Register your models here.


@admin.register(Restaurante)
class RestauranteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'user', 'created')


@admin.register(Horario)
class HorarioAdmin(admin.ModelAdmin):
    list_display = ('user', 'created')


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('user', 'nombre',  'created')
