from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render
from django.views.generic import UpdateView
from .forms import *
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