from __future__ import unicode_literals
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Pasaje, Bus
from events.models import Event

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

class EventAdmin(admin.ModelAdmin):
    list_display = ['day', 'start_time', 'end_time', 'notes']


admin.site.register(CustomUser, CustomUserAdmin) # Funcion para registrar
admin.site.register(Pasaje)
admin.site.register(Event)
