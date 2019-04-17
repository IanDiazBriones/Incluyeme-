from . import views
from django.urls import path, include # new
urlpatterns = [
	path('', views.SignUp.as_view(), name='signup'),
	path('perfil', views.Perfil, name='profile'),
	path('valoracion_a', views.Valoraciones_a, name='valoracion_a'),
	path('valoracion_n', views.Valoraciones_n, name='valoracion_n'),
	path('valoracion_n/<int:pk>/', views.ValoracionUpdate.as_view(), name='valoracion_edit'),
	path('QR/<int:IdentificadorPas>/<int:IdentificadorUsu>/', views.CreateQRCode, name='QR'),
]
