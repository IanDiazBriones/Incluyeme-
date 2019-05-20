from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render
from django.views.generic import UpdateView
from .forms import *
from users.models import *
from django.shortcuts import redirect
from datetime import date
from datetime import datetime, timedelta
import smtplib
# Create your views here.
def ListarSubasta(request):
	subasta= Subasta.objects.all()
	context= {'Subastas': subasta}
	return render(request, 'subasta/subasta_Listar.html', context)

def SubastaDetalle(request, pk):

	subasta = Subasta.objects.get(pk=pk) 
	time1 = datetime.combine(datetime.now(), subasta.HoraF_Subasta)
	TiempoMenos5Min = time1 - timedelta(minutes = 5)
	TiempoRestante =  time1 - datetime.now()
	if TiempoRestante < timedelta(seconds = 0):
		TiempoRestante = "Atrasado"

	context = {
	'Subasta': subasta,
	'TiempoMenos5Min': TiempoMenos5Min,
	'TiempoRestante': TiempoRestante
	}
	return render(request, 'subasta/subasta_verDetalle.html', context)

def SubastaAdd(request, pk):

	now = datetime.now().strftime('%H:%M:%S')
	pasaje = Pasaje.objects.get(pk=pk)
	Cant_Subasta = Subasta.objects.filter(Pasaje_A_Sub = pasaje).count()
	
	if Cant_Subasta == 0:
		subasta = Subasta.objects.create(ValorSubastaActualizado = pasaje.Valor ,Pasaje_A_Sub = pasaje, HoraI_Subasta = now, HoraF_Subasta = pasaje.Hora_Salida, Fecha_Subasta = pasaje.Fecha_Salida
			, Estado_Subasta = False, Estado_Puja = False
			, Ultima_Puja = request.user, Puja = 500)
		time1 = datetime.combine(datetime.now(), subasta.HoraF_Subasta)
		TiempoMenos5Min = time1 - timedelta(minutes = 5)
		TiempoRestante =  time1 - datetime.now()
		if TiempoRestante < timedelta(seconds = 0):
			TiempoRestante = "Terminado"

		context = {
		'Subasta': subasta,
		'TiempoMenos5Min': TiempoMenos5Min,
		'TiempoRestante': TiempoRestante
		}
	else:
		subasta = Subasta.objects.get(Pasaje_A_Sub = pasaje)
		time1 = datetime.combine(datetime.now(), subasta.HoraF_Subasta)
		TiempoMenos5Min = time1 - timedelta(minutes = 5)
		TiempoMenos5Min = datetime.time(TiempoMenos5Min)
		TiempoRestante =  time1 - datetime.now()
		if TiempoRestante < timedelta(seconds = 0):
			TiempoRestante = "Terminado"

		context = {
		'Subasta': subasta,
		'TiempoMenos5Min': TiempoMenos5Min,
		'TiempoRestante': TiempoRestante
		}

	return render(request, 'subasta/Est_Subasta.html', context)

def SubastaPuja(request, pk, pkUsu):
	subasta = Subasta.objects.get(pk=pk)
	User = CustomUser.objects.get(pk=pkUsu)
	subasta.Ultima_Puja = User
	subasta.Pujar()
	return redirect('http://127.0.0.1:8000/subasta/Detalle/'+str(pk)+'/')

def SubastaPagar(request, pk):

	subasta = Subasta.objects.get(pk=pk)
	time1 = datetime.combine(datetime.now(), subasta.HoraF_Subasta)
	TiempoMenos5Min = time1 - timedelta(minutes = 5)
	TiempoRestante =  time1 - datetime.now()
	if TiempoRestante < timedelta(seconds = 0):
		TiempoRestante = "Atrasado"

	context = {
	'Subasta': subasta,
	'TiempoMenos5Min': TiempoMenos5Min,
	'TiempoRestante': TiempoRestante
	}
	return render(request, 'subasta/subasta_Pagar.html', context)


def SubastaResultado(request, pk):
	subasta = Subasta.objects.get(pk=pk) 
	context = {
	'Subasta': subasta,
	}
	return render(request, 'subasta/subasta_Resultado.html', context)

def EstadoPago(request, pk):

	subasta = Subasta.objects.get(pk=pk)
	time1 = datetime.combine(datetime.now(), subasta.HoraF_Subasta)
	TiempoMenos5Min = time1 - timedelta(minutes = 5)
	TiempoRestante =  time1 - datetime.now()
	if TiempoRestante < timedelta(seconds = 0):
		TiempoRestante = "Terminado"

	context = {
	'Subasta': subasta,
	'TiempoMenos5Min': TiempoMenos5Min,
	'TiempoRestante': TiempoRestante
	}
	return render(request, 'subasta/subasta_EstadoPago.html', context)

def EstadoRecibo(request, pk):
	subasta = Subasta.objects.get(pk=pk)
	time1 = datetime.combine(datetime.now(), subasta.HoraF_Subasta)
	TiempoMenos5Min = time1 - timedelta(minutes = 5)
	TiempoRestante =  time1 - datetime.now()
	if TiempoRestante < timedelta(seconds = 0):
		TiempoRestante = "Terminado"
	context = {
	'Subasta': subasta,
	'TiempoMenos5Min': TiempoMenos5Min,
	'TiempoRestante': TiempoRestante
	}
	return render(request, 'subasta/subasta_EstadoRecibo.html', context)


