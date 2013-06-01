from django.shortcuts import render_to_response
from django.template import RequestContext
#from ginecologia.apps.paciente.models import paciente
from ginecologia.apps.login.forms import LoginForm, RegisterUserForm
from django.core.mail import EmailMultiAlternatives

from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

def login_view(request):
	mensaje = ""
	if request.user.is_authenticated():
		return HttpResponseRedirect('/dashboard')
	else :
		if request.method == "POST":
			form = LoginForm(request.POST)
			if form.is_valid():
				username = form.cleaned_data['username']
				password = form.cleaned_data['password']
				usuairo  = authenticate(username=username, password=password)
				if usuairo is not None and usuairo.is_active:
					login(request,usuairo)
					return HttpResponseRedirect('/dashboard')

				else:
					mensaje = "usuario y/o password incorrecto"

		form = LoginForm()
		ctx = {'form' : form, 'mensaje' : mensaje}
		return render_to_response('ginecologo/index.html',ctx,context_instance=RequestContext(request))

def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')
"""
def nombreUSer(request):
	fullname = User.first_name + '' + User.last_name
	ctx = {'nombre' : fullname}
	return render_to_response('ginecologo/dashboard.html', ctx, context_instance=RequestContext(request))"""

def registerView(request):
	form = RegisterUserForm()
	if request.method == 'POST':
		form = RegisterUserForm(request.POST)
		if form.is_valid():
			usuario = form.cleaned_data['username']
			email = form.cleaned_data['email']
			nombre = form.cleaned_data['nombre']
			apellido = form.cleaned_data['apellido']
			password_one = form.cleaned_data['password_one']
			password_two = form.cleaned_data['password_two']
			u = User.objects.create_user(username=usuario, email=email, password=password_one, first_name=nombre, last_name=apellido)
			u.save()#guardar usuario
			return render_to_response('ginecologo/usuarioregistrado.html',context_instance=RequestContext(request))
		else:
			ctx = {'form': form}
			return render_to_response('ginecologo/registroUsuario.html',ctx,context_instance=RequestContext(request))
	ctx = {'form': form}
	return render_to_response('ginecologo/registroUsuario.html',ctx,context_instance=RequestContext(request))