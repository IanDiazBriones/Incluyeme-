from django.shortcuts import render

# Create your views here.
def Foros(request):
	return render(request, 'Foro/Foro.html')


