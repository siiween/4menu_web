# django
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# models


def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('inicio')

    return render(request, 'manager/dashboard.html')
