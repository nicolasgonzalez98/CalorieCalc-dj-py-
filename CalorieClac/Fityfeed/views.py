from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .decorators import *
from django.contrib.auth.models import Group

# Create your views here.
@login_required(login_url='login')
@admin_only
def home(request):
    return render(request, 'main.html')

@unauthorized_user
def loginPage(request):
    return render(request, 'login.html')

@unauthorized_user
def registerPage(request):
    form = crearUsuarioForm()
    if request.method == 'POST':
        form=crearUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            username=form.cleaned_data.get('username')
            group=Group.objects.get(name='user')
            user.groups.add(group)
            email=form.cleaned_data.get('email')
            Cliente.objects.create(usuario=user, nombre=username,email=email)
            return redirect('login')
    ctx = {'form': form}
    return render(request, 'register.html', ctx)