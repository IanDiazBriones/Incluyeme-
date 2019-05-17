from django.db import models
from users.models import CustomUser

class Comentario(models.Model):
    Autor = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    ComentarioU = models.TextField()

    def __str__(self):
        return self.ComentarioU
