from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render
from .models import *


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/signup.html'

# Create your views here.
def Perfil(request):
	Pasajes= Pasaje.objects.all()
	context= {'Pasajes': Pasajes}
	return render(request, 'users/perfil.html', context)
