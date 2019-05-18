from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Pasaje, Bus


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm 
    model = CustomUser #Modelo a seguir
    list_display = ['email', 'nombre', 'telefono', 'es_admin'] #Campos a mostrar
    actions = ["mark_admin", "unmark_admin"]

    def mark_admin(self, request, queryset):
        queryset.update(es_admin=True)

    def unmark_admin(self, request, queryset):
        queryset.update(es_admin=False)




admin.site.register(CustomUser, CustomUserAdmin) # Funcion para registrar
admin.site.register(Pasaje)

