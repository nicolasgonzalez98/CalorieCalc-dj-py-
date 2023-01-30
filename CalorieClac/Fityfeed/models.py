from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Cliente(models.Model):
    usuario = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200, null=True)
    email=models.CharField(max_length=200,null=True)
    fecha_de_creacion=models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return str(self.nombre)

class Categoria(models.Model):
    opciones = (
        (1,'desayuno'),
        (2,'almuerzo'),
        (3,'cena'),
        (4,'snacks'),
    )
    nombre = models.IntegerField(choices=opciones)

    def __str__(self):
        return str(self.nombre)

class ComidaItem(models.Model):
    nombre = models.CharField(max_length=200)
    categoria = models.ManyToManyField(Categoria)
    carbohidratos = models.DecimalField(max_digits=5,decimal_places=2,default=0)
    grasas = models.DecimalField(max_digits=5,decimal_places=2,default=0)
    proteina = models.DecimalField(max_digits=5,decimal_places=2,default=0)
    calorias = models.DecimalField(max_digits=5,decimal_places=2,default=0)
    cantidad = models.IntegerField(default=1,null=True, blank=True)

    def __str__(self):
        return self.nombre

#---Para la pagina del usuario

class UsuarioComidaitem(models.Model):
    cliente = models.ManyToManyField(Cliente, blank=True)
    comida_item = models.ManyToManyField(ComidaItem)