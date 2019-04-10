from django.contrib.auth.models import AbstractUser #Libreria para cambio usuario por defecto
from django.db import models

class CustomUser(AbstractUser):
    # Campos usuario customizado
    email = models.EmailField(unique=True)
    nombre = models.CharField(max_length=35, default=' ')
    telefono = models.IntegerField(default='0')
