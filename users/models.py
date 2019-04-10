from django.contrib.auth.models import AbstractUser #Libreria para cambio usuario por defecto
from django.db import models

class CustomUser(AbstractUser):
    # Campos usuario customizado
    USERNAME_FIELD = 'email'
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    nombre = models.CharField(max_length=35, default=' ')
    telefono = models.IntegerField(default='0')
    REQUIRED_FIELDS = ['username'] # removes email from REQUIRED_FIELDS
