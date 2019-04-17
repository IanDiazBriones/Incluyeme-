from . import views
from django.urls import path, include # new
urlpatterns = [
	path('', views.SignUp.as_view(), name='signup'),
	path('perfil', views.Perfil, name='profile'),
	path('valoracion_a', views.Valoraciones_a, name='valoracion_a'),
	path('valoracion_n', views.Valoraciones_n, name='valoracion_n'),
]
