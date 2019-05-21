from django.shortcuts import render
from subasta.models import *

# Create your views here.
def index(request):
	return render(request, 'pagStatic/index.html')

def WebPay(request, pk):
	context={'pk':pk}
	return render(request, 'pagStatic/WebPay.html',context)

def BancoLogin(request, pk):
	context={'pk':pk}
	return render(request, 'pagStatic/BancoLogin.html',context)

def BancoPago(request, pk):
	subasta= Subasta.objects.get(pk=pk)
	context= {'Subasta': subasta}
	return render(request, 'pagStatic/BancoPagar.html',context)
