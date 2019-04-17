from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render
from .models import *
from django.views.generic import UpdateView
from .forms import *


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/signup.html'

# Create your views here.
def Perfil(request):
	Pasajes= Pasaje.objects.all()
	context= {'Pasajes': Pasajes}
	return render(request, 'users/perfil.html', context)

def Valoraciones_a(request):
	Pasajes= Pasaje.objects.all()
	context= {'Pasajes': Pasajes}
	return render(request, 'users/admin_v.html', context)

def Valoraciones_n(request):
    return render(request, 'users/normal_user_v.html')

class ValoracionUpdate(UpdateView):
    model = Pasaje
    form_class = FormValoraciones
    success_url = reverse_lazy('profile')
    template_name = 'users/normal_user_v.html'

def Lista_Usuarios(request):
    usuario=CustomUser.objects.all()
    context={'usuarios':usuario}
    return render(request, 'users/user_list.html',context)