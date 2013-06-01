# -*- coding: utf8 -*-
from django import forms
from django.contrib.auth.models import User
class LoginForm(forms.Form):
	username = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'Usuario'}))
	password = forms.CharField(label="",widget=forms.PasswordInput(render_value=False, attrs={'placeholder': 'Contraseña'}))

class RegisterUserForm (forms.Form):
	username  = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder':'Nombre de Usuario', 'id': 'newUser'}))
	email     = forms.EmailField(label='',widget=forms.TextInput(attrs={'placeholder': 'Email', 'id': 'newUseremail'}))
	nombre    = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Nombre'}))
	apellido  = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Apellidos'}))
	password_one = forms.CharField(label='',widget=forms.PasswordInput(attrs={'placeholder' : 'Password' , 'id': 'newUserpass1'},render_value=False))
	password_two = forms.CharField(label='',widget=forms.PasswordInput(render_value=False,attrs={'placeholder' : 'Confirma Password', 'id': 'newUserpass2'}))

	def clean_username(self):
		username = self.cleaned_data['username']
		try:
			u = User.objects.get(username=username)
		except User.DoesNotExist:
			return username
		raise forms.ValidationError('Nombre de usuario ya existe')
		
	def clean_email(self):
		email = self.cleaned_data['email']
		try:
			u = User.objects.get(email=email)
		except User.DoesNotExist:
			return email
		raise forms.ValidationError('Email ya existe')

	def clean_password_two(self):
		password_one = self.cleaned_data['password_one']
		password_two = self.cleaned_data['password_two']
		if password_one == password_two:
			pass
		else:
			raise forms.ValidationError('Password no coinciden')

