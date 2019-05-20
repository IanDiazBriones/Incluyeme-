from . import views
from django.urls import path, include # new
urlpatterns = [
	path('listar', views.ListarSubasta, name='ListarSubasta'),
	path('Detalle/<int:pk>/', views.SubastaDetalle, name='DetalleSubasta'),
	path('Estado/<int:pk>/', views.SubastaAdd, name='EstadoSubasta'),
	path('SubastaPuja/<int:pk>/', views.SubastaPuja, name='EstadoSubasta'),
	path('SubastaPagar/<int:pk>/', views.SubastaPagar, name='PagarSubasta'),
	path('SubastaResultado/<int:pk>/', views.SubastaResultado, name='ResultadoSubasta')
	]

