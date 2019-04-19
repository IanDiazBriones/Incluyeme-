from django.db import models

 # Create your models here.

class Bus(models.Model):
    Patente = models.CharField(null=False, max_length=8, unique=True)
    Marca = models.CharField(max_length=30)
    Modelo = models.CharField(max_length=30)

    def DarPatente(self):
        return self.Patente

    def __str__(self):
        return self.DarPatente() 