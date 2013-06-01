# -*- coding: utf8 -*-
from django import forms
from django.forms import ModelForm
from ginecologia.apps.paciente.models import paciente, Sangre

class AltaPacienteFrom(ModelForm):
	fechaNac	= forms.DateField(label='Fecha de Nacimiento',widget=forms.DateInput(attrs={'id': 'hapbirth', 'type':'date'}))
	fechaCons   = forms.DateField(label='Fecha de Consulta', widget=forms.DateInput(attrs={'id':'date', 'type': 'date'}))
	telefonocasa = forms.CharField(label="Telefono de Casa")
	nombreEsposo = forms.CharField(label="Nombre Esposo")
	telAviso     = forms.CharField(label="Telefono de Aviso")
	telcasa 	 = forms.CharField(label='Telegono Casa')
	nomFiscal	 = forms.CharField(label='Nombre Fiscal')
	dirFiscal	 = forms.CharField(label='Direccion Fiscal')

	class Meta:
		model = paciente
	














	#fields = ['sangre']
	#exclude = {'status',}

	#nombre 			= forms.CharField(label='Nombre Completo',widget=forms.TextInput(attrs={'id': 'name', 'class' : 'span input' }))
	#fechaNac 		= forms.DateField(label='Fecha de Nacimiento',widget=forms.DateInput(attrs={'id': 'hapbirth'}))
	#fechaCons		= forms.DateField(label='Fecha de Consulta',widget=forms.DateTimeInput(attrs={'id': 'date'}))
	#telefonocasa	= forms.CharField(label='Telefono Casa',widget=forms.TextInput(attrs={'id': 'telhome'}))
	#direccion 		= forms.CharField(label='Direccón',widget=forms.TextInput(attrs={'id': 'adress', 'class' : 'span input'} ))
	#email			= forms.EmailField(label='Email',widget=forms.TextInput(attrs={'id': 'email'}))
	#ocupacion		= forms.CharField(label='Ocupacion',widget=forms.TextInput(attrs={'id': 'occuption'}))
	#sangre			= forms.IntegerField(label='Sangre',widget=forms.Select(attrs={'id': 'blood'}))
	#nombreEsposo	= forms.CharField(label='Nombre Esposo',widget=forms.TextInput(attrs={'id': 'husband', 'class' : 'span input'}))
	#telAviso 		= forms.CharField(label='Telefono Avisar',widget=forms.TextInput(attrs={'id': 'telnoticeH'}))
	#telcasa 		= forms.CharField(label='Telegono Casa',widget=forms.TextInput(attrs={'id': 'telhomeH'}))
	#movil_id		= forms.CharField(label='Telefono Movil',widget=forms.TextInput(attrs={'id': 'mobilH'}))
	#rfc				= forms.CharField(label='RFC',widget=forms.TextInput(attrs={'id': 'rfc'}))
	#nomFiscal		= forms.CharField(label='Nombre Fiscal',widget=forms.TextInput(attrs={'id': 'namefiscal', 'class' : 'span input'}))
	#dirFiscal		= forms.CharField(label='Direccion Fiscal',widget=forms.TextInput(attrs={'id': 'adressFis', 'class' : 'span input'}))
	#concepto		= forms.CharField(label='Concepto',widget=forms.TextInput(attrs={'id': 'concept'}))
	#importe			= forms.DecimalField(label='Importe',widget=forms.TextInput(attrs={'id': 'amounts'}), decimal_places=2, min_value=0)
	#def clean(self):
		#return self.cleaned_data
	#status			= forms.BooleanField(widget=forms.CheckBoxInput)