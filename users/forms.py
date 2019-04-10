from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm # Librerias para usuario Customizado
from .models import CustomUser # Librerias para usuario Customizado

#Archivo que maneja el formulario de registro

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser # Modelo a seguir dentro de models.py
        fields = ('email', 'nombre', 'telefono') #Campos del formulario

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser # Modelo a seguir dentro de models.py
        fields = ('email', 'nombre', 'telefono') #Campos del formulario