from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('login/', auth_views.LoginView.as_view(template_name='public/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='public/logout.html'), name='logout'),
    path('terminos/', views.terminos, name='terminos'),
    path('registro/', views.singup, name='singup'),
    path('buscar/', views.buscador, name='buscar'),
    path('@<str:username>/', views.local, name='local'),
    path('descargar/<str:id>/', views.descargar, name='descargar'),
]
