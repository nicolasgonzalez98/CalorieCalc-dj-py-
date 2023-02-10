from django.forms import ModelForm
from .models import * 
from django.contrib.auth.forms import UserCreationForm

class ComidaItemForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ComidaItemForm, self).__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs = {
            'id':'name',
            'class':'form-control',
        }
        self.fields['categoria'].widget.attrs = {
            'id':'category',
            'class':'form-control'
        }
        self.fields['carbohidratos'].widget.attrs = {
            'id':'carbohidratos',
            'class':'form-control',
        }
        self.fields['grasas'].widget.attrs = {
            'id':'grasas',
            'class':'form-control',
        }
        self.fields['proteina'].widget.attrs = {
            'id':'proteina',
            'class':'form-control',
        }
        self.fields['calorias'].widget.attrs = {
            'id':'calorias',
            'class':'form-control',
        }
        self.fields['cantidad'].widget.attrs = {
            'id':'cantidad',
            'class':'form-control',
        }
    class Meta:
        model = ComidaItem
        fields="__all__"

class agregarUsuarioComidaItemForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(agregarUsuarioComidaItemForm, self).__init__(*args, **kwargs)
        self.fields['cliente'].widget.attrs = {
            'class':'form-control',
            'id':'cliente'
        }
        self.fields['comida_item'].widget.attrs = {
            'class':'form-control',
            'id':'comida_item'
        }
    class Meta:
        model = UsuarioComidaitem
        fields = "__all__"

class crearUsuarioForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(crearUsuarioForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs = {
            'placeholder': 'Ingrese usuario',
            'class':'form-control',
            'id':'username'
        }
        self.fields['email'].widget.attrs = {
            'class':'form-control',
            'placeholder':'ejemplo@gmail.com',
            'id':'email'
        }
        self.fields['password1'].widget.attrs = {
            'placeholder': '*******',
            'class':'form-control',
            'id':'password1'
        }
        self.fields['password2'].widget.attrs = {
            'placeholder': '*******',
            'class':'form-control',
            'id':'password2'
        }
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']