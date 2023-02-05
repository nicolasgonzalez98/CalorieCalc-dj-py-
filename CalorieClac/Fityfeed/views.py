from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .decorators import *
from django.contrib.auth.models import Group

# Create your views here.


@login_required(login_url='login')
@admin_only
def home(request):
    desayuno = Categoria.objects.filter(nombre='desayuno')[0].comidaitem_set.all()
    almuerzo = Categoria.objects.filter(nombre='almuerzo')[0].comidaitem_set.all()
    cena = Categoria.objects.filter(nombre='cena')[0].comidaitem_set.all()
    snack = Categoria.objects.filter(nombre='snacks')[0].comidaitem_set.all()
    clientes = Cliente.objects.all()
    ctx = {
        'desayuno':desayuno,
        'almuerzo': almuerzo,
        'cena':cena,
        'snack':snack,
        'clientes':clientes
    }
    print(snack)
    return render(request, 'main.html', ctx)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def food_item(request):
    desayuno = Categoria.objects.filter(nombre='desayuno')
    almuerzo = Categoria.objects.filter(nombre='almuerzo')
    cena = Categoria.objects.filter(nombre='cena')
    snack = Categoria.objects.filter(nombre='snack')
    clientes = Cliente.objects.all()
    ctx = {
        'desayuno':desayuno,
        'almuerzo': almuerzo,
        'cena':cena,
        'snack':snack,
        'clientes':clientes
    }
    return render(request, 'foodItem.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def createFoodItem(request):
    form = ComidaItemForm()
    if(request.method == 'POST'):
        form = ComidaItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    ctx = {'form':form}
    return render(request, 'createFoodItem.html', ctx)

@unauthorized_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request,'username or password is invalid')
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

##FALTAN DATOS

def userPage(request):
    return render(request, 'user.html')

@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('login') 

def addFoodUserItem(request):
    user = request.user
    cust = user.cliente
    if request.method == 'POST':
        form = agregarUsuarioComidaItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    form = agregarUsuarioComidaItemForm()
    
    ctx = {'form':form}
    return render(request, 'addFoodUserItem.html', ctx)