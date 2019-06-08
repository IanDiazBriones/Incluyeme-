from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render
from django.views.generic import UpdateView
from .forms import *
from users.models import *
from django.shortcuts import redirect
from datetime import date
from datetime import datetime, timedelta
import smtplib
from background_task import background
# Create your views here.
def ListarSubasta(request):
	subasta= Subasta.objects.all().order_by('ValorSubastaActualizado')
	context= {'Subastas': subasta}
	return render(request, 'subasta/subasta_Listar.html', context)

def SubastaDetalle(request, pk):

	subasta = Subasta.objects.get(pk=pk) 
	time1 = datetime.combine(datetime.now(), subasta.HoraF_Subasta)
	TiempoMenos5Min = time1 - timedelta(minutes = 5)
	TiempoRestante =  TiempoMenos5Min - datetime.now()
	if TiempoRestante < timedelta(seconds = 0):
		TiempoRestante = "Atrasado"

	context = {
	'Subasta': subasta,
	'TiempoMenos5Min': TiempoMenos5Min,
	'TiempoRestante': TiempoRestante
	}
	return render(request, 'subasta/subasta_verDetalle.html', context)

def SubastaAdd(request, pk):

	now = datetime.now().strftime('%H:%M:%S')
	pasaje = Pasaje.objects.get(pk=pk)
	Cant_Subasta = Subasta.objects.filter(Pasaje_A_Sub = pasaje).count()
	
	if Cant_Subasta == 0:
		subasta = Subasta.objects.create(ValorSubastaActualizado = pasaje.Valor ,Pasaje_A_Sub = pasaje, HoraI_Subasta = now, HoraF_Subasta = pasaje.Hora_Salida, Fecha_Subasta = pasaje.Fecha_Salida
			, Estado_Subasta = False, Estado_Puja = False
			, Ultima_Puja = request.user, Puja = 500)
		time1 = datetime.combine(datetime.now(), subasta.HoraF_Subasta)
		TiempoMenos5Min = time1 - timedelta(minutes = 5)
		TiempoRestante =  time1 - datetime.now()
		if TiempoRestante < timedelta(seconds = 0):
			TiempoRestante = "Terminado"

		context = {
		'Subasta': subasta,
		'TiempoMenos5Min': TiempoMenos5Min,
		'TiempoRestante': TiempoRestante
		}
	else:
		subasta = Subasta.objects.get(Pasaje_A_Sub = pasaje)
		time1 = datetime.combine(datetime.now(), subasta.HoraF_Subasta)
		TiempoMenos5Min = time1 - timedelta(minutes = 5)
		TiempoMenos5Min = datetime.time(TiempoMenos5Min)
		TiempoRestante =  time1 - datetime.now()
		subasta.ReactivarSub()
		if TiempoRestante < timedelta(seconds = 0):
			TiempoRestante = "Terminado"

		context = {
		'Subasta': subasta,
		'TiempoMenos5Min': TiempoMenos5Min,
		'TiempoRestante': TiempoRestante
		}

	return render(request, 'subasta/Est_Subasta.html', context)

def SubastaPuja(request, pk, pkUsu):
	subasta = Subasta.objects.get(pk=pk)
	User = CustomUser.objects.get(pk=pkUsu)
	subasta.Ultima_Puja = User
	subasta.Pujar()
	return redirect('/subasta/Detalle/'+str(pk)+'/')

def CancelarSub(request, idSub):
	subasta = Subasta.objects.get(pk=idSub)
	subasta.Cancelar()
	return redirect('/user/perfil')

def SubastaPagar(request, pk):

	subasta = Subasta.objects.get(pk=pk)
	time1 = datetime.combine(datetime.now(), subasta.HoraF_Subasta)
	TiempoMenos5Min = time1 - timedelta(minutes = 5)
	TiempoRestante =  time1 - datetime.now()
	if TiempoRestante < timedelta(seconds = 0):
		TiempoRestante = "Atrasado"

	context = {
	'Subasta': subasta,
	'TiempoMenos5Min': TiempoMenos5Min,
	'TiempoRestante': TiempoRestante
	}
	return render(request, 'subasta/subasta_Pagar.html', context)


def SubastaResultado(request, pk):
	subasta = Subasta.objects.get(pk=pk)
	mensaje = "Su pasaje con destino a "+subasta.Pasaje_A_Sub.Destino+" sido vendido satisfactoriamente"
	asunto = "Pasaje vendido satisfactoriamente"
	EnvioCorreosSub(mensaje, asunto, subasta.Pasaje_A_Sub.Dueño.email)
	mensaje = "Su pasaje adquirido en la subasta con destino a "+subasta.Pasaje_A_Sub.Destino+" fue comprado satisfactoriamente \nSu url para su codigo QR : http://127.0.0.1:8000/user/QR/"+str(subasta.Pasaje_A_Sub.pk)+"/"+str(subasta.Pasaje_A_Sub.Dueño.pk)+"/"
	asunto = "Pasaje Comprado satisfactoriamente"
	EnvioCorreosSub(mensaje, asunto, subasta.Ultima_Puja.email)
	subasta.Pasaje_A_Sub.Dueño = subasta.Ultima_Puja
	context = {
	'Subasta': subasta,
	}
	return render(request, 'subasta/subasta_Resultado.html', context)

def EnvioCorreosSub(mensaje, asunto, correo):
	Remitente = 'milos.incluyeme@gmail.com'
	print(correo)
	Destinatario = correo
	Pass = 'incluyeme123'

	message = (mensaje)
	subject = asunto
	message = 'Subject: {}\n\n{}'.format(subject, message)

	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(Remitente, Pass)
	server.sendmail(Remitente, Destinatario, message)
	server.quit()

def EstadoPago(request, pk):

	subasta = Subasta.objects.get(pk=pk)
	time1 = datetime.combine(datetime.now(), subasta.HoraF_Subasta)
	TiempoMenos5Min = time1 - timedelta(minutes = 5)
	TiempoRestante =  time1 - datetime.now()
	if TiempoRestante < timedelta(seconds = 0):
		TiempoRestante = "Terminado"

	context = {
	'Subasta': subasta,
	'TiempoMenos5Min': TiempoMenos5Min,
	'TiempoRestante': TiempoRestante
	}
	return render(request, 'subasta/subasta_EstadoPago.html', context)

def EstadoRecibo(request, pk):
	subasta = Subasta.objects.get(pk=pk)
	time1 = datetime.combine(datetime.now(), subasta.HoraF_Subasta)
	TiempoMenos5Min = time1 - timedelta(minutes = 5)
	TiempoRestante =  time1 - datetime.now()
	if TiempoRestante < timedelta(seconds = 0):
		TiempoRestante = "Terminado"
	context = {
	'Subasta': subasta,
	'TiempoMenos5Min': TiempoMenos5Min,
	'TiempoRestante': TiempoRestante
	}
	return render(request, 'subasta/subasta_EstadoRecibo.html', context)

@background(schedule=5)
def MSGnotificacionPago():
  #Traer los objetos pasajes de la BD
  Subastas= Subasta.objects.all()
  #Por cada uno de los pasajes dentro del array
  print ("Hola Mundo")
  for var in Subastas:
    #Condiciones que la fecha de hoy sea igual a la fecha de salida del pasaje
    #y que no se enviara una notificacion anteriormente 
    Fecha_Y_Hora_Pasaje = datetime.combine(var.Fecha_Subasta, var.HoraF_Subasta)
    Horas_Antes_Pasaje = Fecha_Y_Hora_Pasaje - timedelta(minutes = 5)
    if (var.Estado_Subasta == False ) and (abs(datetime.now() - Horas_Antes_Pasaje) <= timedelta(minutes = 5) and (var.Estado_Puja == True)):
      var.Estado_Subasta == True
      print((abs(datetime.now() - Horas_Antes_Pasaje) <= timedelta(minutes = 5)))

      #var.Estado_Subasta = True
      Remitente = 'milos.incluyeme@gmail.com'
      Destinatario = var.Ultima_Puja.email
      Pass = 'incluyeme123'

      message = ("Felicitaciones, gano la subasta, su link para pagar es: http://127.0.0.1:8000/subasta/SubastaPagar/"+str(var.pk)+"/")
      subject = 'Recordatorio de viaje'
      message = 'Subject: {}\n\n{}'.format(subject, message)

      server = smtplib.SMTP('smtp.gmail.com', 587)
      server.starttls()
      server.login(Remitente, Pass)
      server.sendmail(Remitente, Destinatario, message)
      server.quit()

@background(schedule=5)
def MSGnotificacionPerdida():
  #Traer los objetos pasajes de la BD
  Subastas= Subasta.objects.all()
  #Por cada uno de los pasajes dentro del array
  for var in Subastas:
    #Condiciones que la fecha de hoy sea igual a la fecha de salida del pasaje
    #y que no se enviara una notificacion anteriormente 
    Fecha_Y_Hora_Pasaje = datetime.combine(var.Fecha_Subasta, var.HoraF_Subasta)
    Horas_Antes_Pasaje = Fecha_Y_Hora_Pasaje - timedelta(minutes = 5)
    if (var.Estado_Subasta == False ) and  (abs(datetime.now() - Horas_Antes_Pasaje) <= timedelta(minutes = 5) and (var.Estado_Puja == False)):
      var.Estado_Subasta == True
      print((abs(datetime.now() - Horas_Antes_Pasaje) <= timedelta(minutes = 5)))

      #var.Estado_Subasta = True
      Remitente = 'milos.incluyeme@gmail.com'
      Destinatario = var.Pasaje_A_Sub.Dueño.email
      Pass = 'incluyeme123'

      message = ("Felicitaciones, gano la subasta, su link para pagar es: http://127.0.0.1:8000/subasta/SubastaPagar/"+str(var.pk)+"/")
      subject = 'Recordatorio de viaje'
      message = 'Subject: {}\n\n{}'.format(subject, message)

      server = smtplib.SMTP('smtp.gmail.com', 587)
      server.starttls()
      server.login(Remitente, Pass)
      server.sendmail(Remitente, Destinatario, message)
      server.quit()



