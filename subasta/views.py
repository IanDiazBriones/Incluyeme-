from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render
from django.views.generic import UpdateView
from .forms import *
from users.models import Pasaje
from django.shortcuts import redirect
import datetime
# Create your views here.
def ListarSubasta(request):
	subasta= Subasta.objects.all()
	context= {'Subastas': subasta}
	return render(request, 'subasta/subasta_Listar.html', context)

def SubastaDetalle(request, pk):

	subasta = Subasta.objects.get(pk=pk) 

	context = {
	'Subasta': subasta,
	}
	return render(request, 'subasta/subasta_verDetalle.html', context)

def SubastaAdd(request, pk):

	now = datetime.datetime.now().strftime('%H:%M:%S')
	pasaje = Pasaje.objects.get(pk=pk)
	Cant_Subasta = Subasta.objects.filter(Pasaje_A_Sub = pasaje).count()
	
	if Cant_Subasta == 0:
		subasta = Subasta.objects.create(ValorSubastaActualizado = pasaje.Valor ,Pasaje_A_Sub = pasaje, HoraI_Subasta = now, HoraF_Subasta = pasaje.Hora_Salida, Fecha_Subasta = pasaje.Fecha_Salida
			, Estado_Subasta = False, Estado_Puja = False
			, Ultima_Puja = request.user, Puja = 500)
		context = {
		'Subasta': subasta,
		}
	else:
		subasta = Subasta.objects.get(Pasaje_A_Sub = pasaje)
		context = {
		'Subasta': subasta,
		}

	return render(request, 'subasta/Est_Subasta.html', context)

def SubastaPuja(request, pk):
	subasta = Subasta.objects.get(pk=pk)
	subasta.Pujar()
	return redirect('http://127.0.0.1:8000/subasta/Detalle/'+str(pk)+'/')


