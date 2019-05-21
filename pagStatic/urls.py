from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('WebPay/<int:pk>/', views.WebPay, name='WebPay'),
	path('BancoLogin/<int:pk>/', views.BancoLogin, name='BancoLogin'),
]
