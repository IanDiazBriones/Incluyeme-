from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'pagStatic/index.html')

def WebPay(request, pk):
	context={'pk':pk}
	return render(request, 'pagStatic/WebPay.html',context)

def BancoLogin(request, pk):
	context={'pk':pk}
	return render(request, 'pagStatic/BancoLogin.html',context)
