from django.contrib.auth.models import AbstractUser #Libreria para cambio usuario por defecto
from django.db import models
from Buses.models import Bus

class CustomUser(AbstractUser):
    # Campos usuario customizado
    USERNAME_FIELD = 'email'
    username = models.CharField(max_length=150, unique=True)
    rut = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    nombre = models.CharField(max_length=35, default=' ')
    telefono = models.IntegerField(default='0')
    foto = models.ImageField(null=True, blank=True, upload_to='photos/')
    es_admin = models.BooleanField(default= False)


    REQUIRED_FIELDS = ['username'] # removes email from REQUIRED_FIELDS


class Pasaje(models.Model):
    Codigo = models.CharField(max_length=150, unique=True)
    Asiento = models.IntegerField(default='0')
    Fecha_Salida = models.DateField()
    Hora_Salida = models.TimeField()
    PatenteBus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    Dueño = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    Opciones_Valoraciones = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'))
    Valoracion = models.IntegerField(default='0', choices=Opciones_Valoraciones)
    


