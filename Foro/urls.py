from django.urls import path
from Foro import views

urlpatterns = [
	path('Foros', views.Foros, name='Foros'),
]