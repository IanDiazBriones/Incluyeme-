from django.db import models
from users.models import Pasaje
# Create your models here.

class Subasta(models.Model):
    ValorSubastaActualizado = models.IntegerField(default='0')
    Puja = models.IntegerField(default='0')
    HoraI_Subasta = models.TimeField()
    HoraF_Subasta = models.TimeField()
    Fecha_Subasta = models.DateField()
    Estado_Subasta = models.BooleanField(default=False)
    Estado_Puja = models.BooleanField(default=False)
    Pasaje_A_Sub = models.ForeignKey(Pasaje, on_delete=models.CASCADE)
