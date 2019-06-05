from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render
from django.views.generic import UpdateView
from .forms import *
from background_task import background
from datetime import date
from datetime import datetime, timedelta
from twilio.rest import Client
import smtplib

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/signup.html'

# Create your views here.
def Perfil(request):
  PasajesAntesHoy= Pasaje.objects.filter(Fecha_Salida__lte=date.today())
  PasajesDespuesHoy= Pasaje.objects.filter(Fecha_Salida__gte=date.today())
  context= {'PasajesAntesHoy': PasajesAntesHoy,'PasajesDespuesHoy': PasajesDespuesHoy}
  return render(request, 'users/perfil.html', context)

def ListarPatente(request):
    bus = Bus.objects.all()
    context = {'buses': bus}
    return render(request, 'users/retraso_bus.html', context)
  
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

def mostrarProtocolo(request):
    return render(request, 'users/protocolo.html')

def mostrarImagenProtocolo(request):
    return render(request, 'users/imagen_protocolo.html')

def CreateQRCode(request, IdentificadorPas, IdentificadorUsu):
    Pasajes= Pasaje.objects.get(pk = IdentificadorPas)
    Usuario= CustomUser.objects.get(pk = IdentificadorUsu)
    Rut = str(Usuario.rut)
    Nombre = str(Usuario.nombre)
    Email = str(Usuario.email)
    Telefono = str(Usuario.telefono)
    Destino = str(Pasajes.Destino)
    Asiento = str(Pasajes.Asiento)
    Fecha = str(Pasajes.Fecha_Salida)
    Hora = str(Pasajes.Hora_Salida)
    Patente = str(Pasajes.PatenteBus)
    StringQR = str("RUN="+Rut+"/"
                   +"NOMBRE="+Nombre+"/"    
                   +"CELULAR="+Telefono+"/"
                   +"EMAIL="+Email+"/"
                   +"HORA SALIDA="+Hora+"/"
                   +"FECHA SALIDA="+Fecha+"/"
                   +"ASIENTO="+Asiento+"/"
                   +"DESTINO="+Destino+"/"              
                   +"PATENTE="+Patente)
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
      
      print("Codigo Pasaje = " + str(var.Codigo))
      account_sid = "ACb8609460a3a4d8621beba519f081a23b"
      auth_token = "d39131e76c3d581954efbc1e8711e1dc"
      client = Client(account_sid, auth_token)

      message = client.messages.create(
          to=str("+"+str(var.Dueño.telefono)),
          from_="+13345106427",
          body=("Hoy es el dia de su viaje destino a: "+ var.Destino+ "Hora: "+str(var.Hora_Salida)+" Asiento: "+ str(var.Asiento))
      )

      print(message.sid)


      Remitente = 'milos.incluyeme@gmail.com'
      Destinatario = var.Dueño.email
      Pass = 'incluyeme123'

      message = ("Hoy es el dia de su viaje destino a: " + var.Destino + " Hora: "+ str(var.Hora_Salida) + " Asiento: " + str(var.Asiento))
      subject = 'Recordatorio de viaje'
      message = 'Subject: {}\n\n{}'.format(subject, message)

      server = smtplib.SMTP('smtp.gmail.com', 587)
      server.starttls()
      server.login(Remitente, Pass)
      server.sendmail(Remitente, Destinatario, message)
      server.quit()

      #Se actualiza el pasaje cambiando la variable de notificacion a True
      var.EnvioNotificacionDia();


#Retraso desde que se encolo la tarea, para que el sistema la ejecute
@background(schedule=5)
def SMSNotificacion2HRS():
  #Traer los objetos pasajes de la BD
  Pasajes= Pasaje.objects.all()
  #Por cada uno de los pasajes dentro del array
  for var in Pasajes:
    #Condiciones que la fecha de hoy sea igual a la fecha de salida del pasaje
    #y que no se enviara una notificacion anteriormente 
    Fecha_Y_Hora_Pasaje = datetime.combine(var.Fecha_Salida, var.Hora_Salida)
    Horas_Antes_Pasaje = Fecha_Y_Hora_Pasaje - timedelta(hours = 2)
    if (var.NotificacionHorasEnv == False and (abs(datetime.now() - Fecha_Y_Hora_Pasaje) <= timedelta(hours = 2))) :
      #Codigo del envio del sms
      
      #print("Codigo Pasaje = " + str(var.Codigo))
      #account_sid = "ACb8609460a3a4d8621beba519f081a23b"
      #auth_token = "d39131e76c3d581954efbc1e8711e1dc"
      #client = Client(account_sid, auth_token)

      #message = client.messages.create(
          #to=str("+"+str(var.Dueño.telefono)),
          #from_="+13345106427",
          #body=("Hoy es el dia de su viaje destino a: "+ var.Destino+ "Hora: "+str(var.Hora_Salida)+" Asiento: "+ str(var.Asiento))
      #)

      #print(message.sid)

      Remitente = 'milos.incluyeme@gmail.com'
      Destinatario = var.Dueño.email
      Pass = 'incluyeme123'

      message = ("Quedan menos de 2 horas para su viaje destino a: " + var.Destino + " Hora: "+ str(var.Hora_Salida) + " Asiento: " + str(var.Asiento))
      subject = 'Recordatorio de viaje'
      message = 'Subject: {}\n\n{}'.format(subject, message)

      server = smtplib.SMTP('smtp.gmail.com', 587)
      server.starttls()
      server.login(Remitente, Pass)
      server.sendmail(Remitente, Destinatario, message)
      server.quit()

      #Se actualiza el pasaje cambiando la variable de notificacion a True
      var.EnvioNotificacionHoras();
def notificacion(request,elem):
    # Traer los objetos pasajes de la BD
    Pasajes = Pasaje.objects.all()
    for var in Pasajes:
        if var.PatenteBus.Patente == str(elem):
            Remitente = 'milos.incluyeme@gmail.com'
            Destinatario = var.Dueño.email
            Pass = 'incluyeme123'

            message = ("Hemos percibido un retraso por parte del conductor del bus: "+var.PatenteBus.Patente)
            subject = 'Retraso'
            message = 'Subject: {}\n\n{}'.format(subject, message)

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(Remitente, Pass)
            server.sendmail(Remitente, Destinatario, message)
            server.quit()

            #-------------------------------------------
            #Codigo del envio del sms

            print("Codigo Pasaje = " + str(var.Codigo))
            account_sid = "ACb8609460a3a4d8621beba519f081a23b"
            auth_token = "d39131e76c3d581954efbc1e8711e1dc"
            client = Client(account_sid, auth_token)

            message = client.messages.create(
            to=str("+"+str(var.Dueño.telefono)),
            from_="+13345106427",
            body=("Hemos percibido un retraso por parte del conductor del bus: "+var.PatenteBus.Patente))

            print(message.sid)