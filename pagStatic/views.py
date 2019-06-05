from django.shortcuts import render
from subasta.models import *
from django.shortcuts import redirect
# Create your views here.
def index(request):
	Pasajes= Pasaje.objects.all().order_by('-Valoracion')[:5]
	context= {'Pasajes': Pasajes}
	return render(request, 'pagStatic/index.html', context)

def FirstPage(request):
	return redirect('user/login/')

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
