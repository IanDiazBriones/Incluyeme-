from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm # Librerias para usuario Customizado
from .models import * # Librerias para usuario Customizado
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

#Archivo que maneja el formulario de registro

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser # Modelo a seguir dentro de models.py
        fields = ('username', 'rut', 'email', 'nombre', 'telefono', 'foto') #Campos del formulario

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser # Modelo a seguir dentro de models.py
        fields = ('username', 'rut', 'email', 'nombre', 'telefono', 'foto') #Campos del formulario

class FormValoraciones(forms.ModelForm):

    class Meta:
        model = Pasaje # Modelo a seguir dentro de models.py
        fields = ('Valoracion',) #Campos del formulario
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Valorar'))
