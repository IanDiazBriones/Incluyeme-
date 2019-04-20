from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render
from .models import *
from django.views.generic import UpdateView
from .forms import *
from background_task import background
from datetime import date
from datetime import datetime

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

def CreateQRCode(request, IdentificadorPas, IdentificadorUsu):
    Pasajes= Pasaje.objects.get(pk = IdentificadorPas)
    Usuario= CustomUser.objects.get(pk = IdentificadorUsu)
    Nombre = str(Usuario.nombre)
    Rut = str(Usuario.rut)
    Email = str(Usuario.email)
    Telefono = str(Usuario.telefono)
    Destino = str(Pasajes.Destino)
    Codigo = str(Pasajes.Codigo)
    Asiento = str(Pasajes.Asiento)
    Fecha = str(Pasajes.Fecha_Salida)
    Hora = str(Pasajes.Hora_Salida)
    StringQR = str(Codigo+"/"
                   +Asiento+"/"
                   +Fecha+"/"
                   +Hora+"/"
                   +Destino+"/"              
                   +Nombre+"/"
                   +Rut+"/"
                   +Email+"/"
                   +Telefono+"/")
    context= {'QRString': StringQR}
    return render(request, 'users/QR.html', context)

#Retraso desde que se encolo la tarea, para que el sistema la ejecute
@background(schedule=5)
def SMSNotificacionDia():
  #Traer los objetos pasajes de la BD
  Pasajes= Pasaje.objects.all()
  #Por cada uno de los pasajes dentro del array
  for var in Pasajes:
    #Condiciones que la fecha de hoy sea igual a la fecha de salida del pasaje
    #y que no se enviara una notificacion anteriormente 
    if (date.today() == var.Fecha_Salida and var.NotificacionDiaEnv == False):
      #Codigo del envio del sms
      print(var.Fecha_Salida)
      print(var.NotificacionDiaEnv)
      #Se actualiza el pasaje cambiando la variable de notificacion a True
      var.EnvioNotificacionDia();
      