from django.shortcuts import render
from .forms import CommentForm
from django.shortcuts import redirect

# Create your views here.
def Foros(request):
	return render(request, 'Foro/Foro.html')


