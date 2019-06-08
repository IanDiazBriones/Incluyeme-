from . import views
from django.urls import path, include # new
from .views import MSGnotificacionPago, MSGnotificacionPerdida
urlpatterns = [
	path('listar', views.ListarSubasta, name='ListarSubasta'),
	path('Detalle/<int:pk>/', views.SubastaDetalle, name='DetalleSubasta'),
	path('Estado/<int:pk>/', views.SubastaAdd, name='EstadoSubasta'),
	path('SubastaPuja/<int:pk>/<int:pkUsu>/', views.SubastaPuja, name='PujaSubasta'),
	path('SubastaPagar/<int:pk>/', views.SubastaPagar, name='PagarSubasta'),
	path('SubastaResultado/<int:pk>/', views.SubastaResultado, name='ResultadoSubasta'),
	path('EstadoPago/<int:pk>/', views.EstadoPago, name='EstadoPago'),
	path('EstadoRecibo/<int:pk>/', views.EstadoRecibo, name='EstadoRecibo'),
	path('CancelaSub/<int:idSub>/', views.CancelarSub, name='Cancela'),
	]

# Para que se empiece el proceso de tareas se debe ejecutar por consola "python manager.py process_tasks"
# repeat = cada cuanto se ejecutara la tarea en segundos
# repeat_until = cuantas veces se repetira (None = para siempre)
MSGnotificacionPago(repeat=10,repeat_until=None)
MSGnotificacionPerdida(repeat=10,repeat_until=None)