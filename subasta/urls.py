from . import views
from django.urls import path, include # new
urlpatterns = [
	path('listar', views.ListarSubasta, name='ListarSubasta'),
	path('Detalle/<int:pk>/', views.SubastaDetalle, name='DetalleSubasta'),
	path('Estado/<int:pk>/', views.SubastaAdd, name='EstadoSubasta'),
	path('SubastaPuja/<int:pk>/<int:pkUsu>/', views.SubastaPuja, name='PujaSubasta'),
	path('SubastaPagar/<int:pk>/', views.SubastaPagar, name='PagarSubasta'),
	path('SubastaResultado/<int:pk>/', views.SubastaResultado, name='ResultadoSubasta'),
	path('EstadoPago/<int:pk>/', views.EstadoPago, name='EstadoPago'),
	path('EstadoRecibo/<int:pk>/', views.EstadoRecibo, name='EstadoRecibo')
	]

