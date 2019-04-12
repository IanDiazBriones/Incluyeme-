from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/signup.html'

# Create your views here.
def Perfil(request):
	return render(request, 'users/perfil.html')