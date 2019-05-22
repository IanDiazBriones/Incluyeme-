from django.db import models
from django.urls import reverse

class Event(models.Model):
    title = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()



