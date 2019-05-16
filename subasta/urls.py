from . import views
from django.urls import path, include # new
urlpatterns = [
	path('listar', views.ListarSubasta, name='ListarSubasta'),

]

