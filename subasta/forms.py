from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm # Librerias para usuario Customizado
from .models import * # Librerias para usuario Customizado
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit



class FormSubastaAdd(forms.ModelForm):

    class Meta:
        model = Subasta # Modelo a seguir dentro de models.py
        fields = ('ValorSubastaActualizado', 'HoraF_Subasta', 'ValorSubastaActualizado', 'Pasaje_A_Sub',) #Campos del formulario
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Valorar'))