from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.dashboard, name='dashboard-manager'),
    path('crear/menu/', views.crearMenu, name='crearMenu'),
    path('completar/perfil/', views.completarPerfil, name='completarPerfil'),
    path('ajustes/perfil/', views.ajustes, name='ajustes'),
    path('ajustes/password/', views.password, name='password'),
    path('eliminar/menu/<str:id>', views.eliminarMenu, name='eliminarMenu'),
    path('modificar/menu/<str:id>', views.modificarMenu, name='modificarMenu'),
    path('modificar/imagen/', views.modificarImagen, name='modificarImagen'),
    path('modificar/datos/publicos/', views.modificarDatosPublicos, name='modificarDatosPublicos'),
    path('modificar/direccion/', views.modificarDireccion, name='modificarDireccion'),
    path('modificar/horario/', views.modificarHorario, name='modificarHorario'),
]
