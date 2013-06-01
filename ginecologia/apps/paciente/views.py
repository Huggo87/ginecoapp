# Create your views here.
# -*- coding: utf8 -*-
from datetime import date
from django.shortcuts import render_to_response
from django.template import RequestContext
from ginecologia.apps.paciente.models import paciente, Sangre
from ginecologia.apps.paciente.forms import AltaPacienteFrom
from django.core.mail import EmailMultiAlternatives ,EmailMessage#Enviamos HTML
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

def dashboard_view(request):
	if request.user.is_authenticated():
		mensaje = "Dashboard."
		##happyday = date.today() #dia de hoy
		pacientes = paciente.objects.all().count()
		dia = 	date.today().day
		mes =   date.today().month
		#semana = date.
		happyday = paciente.objects.filter(fechaNac__day=dia, fechaNac__month=mes).count()
        
		if happyday > 0:
			person = paciente.objects.filter(fechaNac__day=dia, fechaNac__month=mes)
			#cumple = map(str,person)
			to_amin = 'gilmur_eclipse@hotmail.com'
			html_content = 'Recordatorio de cumpleños <br><br>****Hoy es cumplaños de ***<br>%s'%(map(str,person))
			msg = EmailMultiAlternatives('Correo Cumpleañeras',html_content,'from@server.com',[to_amin])
			msg.attach_alternative(html_content, 'text/html') #defino el contenido ocomo html
			msg.send()#Envio el correo
			enviar = True

		
		ctx 	= {'msj':mensaje,  'day':dia , 'month':mes, 'pacientes':pacientes, 'happyday':happyday, 'enviar':enviar}

		return render_to_response('ginecologo/dashboard.html', ctx,  context_instance=RequestContext(request))
	else:
		enviar = False
		return HttpResponseRedirect('/')


def alta_paciente_view(request):
	
	if request.user.is_authenticated():
		info = " "
		if request.method == "POST":
			formulario = AltaPacienteFrom(request.POST)
			formulario.sangre = 1
			if formulario.is_valid():
				formulario.save()
				info = "Se ha Guardado satisfactoriamente"
			else:
				info = "Datos incorrectos verifica la informacion"
		else:
			info = " "
			formulario = AltaPacienteFrom()
		mensaje = "Alta Paciente."	
		ctx 	= {'form' : formulario,'msj' : mensaje, 'info':info}
		return render_to_response('ginecologo/altanuevopaciente.html', ctx, context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/')
