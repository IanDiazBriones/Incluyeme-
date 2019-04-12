from . import views
from django.urls import path, include # new
urlpatterns = [
	path('', views.SignUp.as_view(), name='signup'),
	path('perfil', views.Perfil, name='profile'),
]
