from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .decorators import *
from django.contrib.auth.models import Group
from .filters import foodItemFilter

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
    desayuno = Categoria.objects.filter(nombre='desayuno')[0].comidaitem_set.all()
    almuerzo = Categoria.objects.filter(nombre='almuerzo')[0].comidaitem_set.all()
    cena = Categoria.objects.filter(nombre='cena')[0].comidaitem_set.all()
    snack = Categoria.objects.filter(nombre='snacks')[0].comidaitem_set.all()
    bcnt = desayuno.count()
    acnt = almuerzo.count()
    ccnt = cena.count()
    scnt = snack.count()
    ctx = {
        'desayuno':desayuno,
        'almuerzo': almuerzo,
        'cena':cena,
        'snack':snack,
        'bcnt':bcnt,
        'acnt': acnt,
        'ccnt':ccnt,
        'scnt':scnt
    }
    print(cena)
    return render(request, 'foodItem.html', ctx)

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
    user = request.user
    cust=user.cliente
    alimentos = ComidaItem.objects.filter()
    my_filter = foodItemFilter(request.GET, queryset=alimentos)
    print(my_filter)
    alimentos = my_filter.qs
    total = UsuarioComidaitem.objects.all()
    mis_alimentos = total.filter(cliente = cust)
    cnt = mis_alimentos.count()
    querySetFood = []
    
    for c in mis_alimentos:
        querySetFood.append(c.comida_item.all())
    alimentos_finales = []
    for i in querySetFood:
        for alim in i:
            alimentos_finales.append(alim)
    calorias_totales = 0
    for alim in alimentos_finales:
        calorias_totales += alim.calorias
    calorias_faltantes = 2000 - calorias_totales
    ctx = {
        'calorias_faltantes': calorias_faltantes,
        'calorias_totales': calorias_totales,
        'cnt':cnt,
        'my_filter':my_filter,
        'alimentos_finales':alimentos_finales,
        'alimentos':alimentos
    }
    return render(request, 'user.html', ctx)

@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('login') 

def addFoodUserItem(request):
    user = request.user
    # cust = user.cliente
    if request.method == 'POST':
        form = agregarUsuarioComidaItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    form = agregarUsuarioComidaItemForm()
    
    ctx = {'form':form}
    return render(request, 'addFoodUserItem.html', ctx)