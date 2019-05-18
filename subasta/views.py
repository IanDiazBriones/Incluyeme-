from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render
from django.views.generic import UpdateView
from .forms import *
from users.models import Pasaje
import datetime
from django.utils.timezone import utc
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

	now = datetime.datetime.utcnow().replace(tzinfo=utc)
	pasaje = Pasaje.objects.get(pk=pk)
	subasta = Subasta.objects.create(ValorSubastaActualizado = pasaje.Valor ,Pasaje_A_Sub = pasaje, HoraI_Subasta = pasaje.Hora_Salida, HoraF_Subasta = pasaje.Hora_Salida, Fecha_Subasta = pasaje.Fecha_Salida
		, Estado_Subasta = False, Estado_Puja = False
		, Ultima_Puja = request.user, Puja = 500)

	context = {
	'Subasta': subasta,
	}
	return render(request, 'subasta/Est_Subasta.html', context)


