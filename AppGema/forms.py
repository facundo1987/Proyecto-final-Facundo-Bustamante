from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class HuespedFormulario (forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    correo = forms.EmailField()
    
class ReservaFormulario (forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    checkin = forms.DateField()
    checkout = forms.DateField()

class AvatarFormulario(forms.Form):
    imagen =forms.ImageField()      

class UsuarioRegistro (UserCreationForm):
    
    email = forms.EmailField()
    password1 = forms.CharField(label = "contraseña", widget = forms.PasswordInput)
    password2 = forms.CharField(label = "Repetir la contraseña", widget = forms.PasswordInput)
    
    class Meta:
        
        model = User
        fields = ["username", "email", "first_name", "last_name", "password1", "password2" ]
        



class EditarUsuario (UserChangeForm):

    password = None
    
    class Meta:
        
        model = User
        fields = ["email", "first_name", "last_name" ]
        
        
  