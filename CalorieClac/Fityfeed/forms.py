from django.forms import ModelForm
from .models import * 
from django.contrib.auth.forms import UserCreationForm

class ComidaItemForm(ModelForm):
    class Meta:
        model = ComidaItem
        fields="__all__"

class agregarUsuarioComidaItemForm(ModelForm):
    class Meta:
        model = UsuarioComidaitem
        fields = "__all__"

class crearUsuarioForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']