from . import views
from django.urls import path, include # new
from users.views import SMSNotificacionDia, SMSNotificacion2HRS
urlpatterns = [
	path('Registro/', views.SignUp.as_view(), name='signup'),
	path('perfil', views.Perfil, name='profile'),
	path('valoracion_a', views.Valoraciones_a, name='valoracion_a'),
	path('valoracion_n', views.Valoraciones_n, name='valoracion_n'),
	path('valoracion_n/<int:pk>/', views.ValoracionUpdate.as_view(), name='valoracion_edit'),
	path('listar',views.Lista_Usuarios,name='LISTADEUSUARIOS'),
	path('QR/<int:IdentificadorPas>/<int:IdentificadorUsu>/', views.CreateQRCode, name='QR'),
	path('Protocolo', views.mostrarProtocolo, name='proto'),
	path('MostrarProtocolo', views.mostrarImagenProtocolo, name='mostrar_image'),
	path('retraso',views.ListarPatente, name='retrasobus'),
	path('NotificacionPasajeros', views.Patente, name='NotificacionPasajeros'),
	path('notificacion/<slug:elem>', views.notificacion, name='notificacion'),
	path('notificacionAdmin/<slug:elem>', views.notificacionA, name='notificacionAdmin'),

]


# Para que se empiece el proceso de tareas se debe ejecutar por consola "python manager.py process_tasks"
# repeat = cada cuanto se ejecutara la tarea en segundos
# repeat_until = cuantas veces se repetira (None = para siempre)
SMSNotificacionDia(repeat=86400,repeat_until=None)

SMSNotificacion2HRS(repeat=7200,repeat_until=None)