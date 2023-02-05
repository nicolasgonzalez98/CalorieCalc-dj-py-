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