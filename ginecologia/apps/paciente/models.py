from django.db import models

# Create your models here.
class Sangre(models.Model):
	tipo = models.CharField(max_length=20)

	def __unicode__(self):
		return self.tipo

class paciente(models.Model):
	nombre 			= models.CharField(max_length=50)
	fechaNac		= models.DateField(auto_now=False, blank=False)
	fechaCons		= models.DateTimeField(auto_now=False, blank=False)
	telefonocasa	= models.CharField(null=True, max_length=10)
	direccion 		= models.CharField(max_length=100)
	email			= models.EmailField(null=True)
	ocupacion		= models.CharField(null=False, max_length=10)
	sangre			= models.ForeignKey(Sangre)
	nombreEsposo	= models.CharField(max_length=50)
	telAviso 		= models.CharField(max_length=10)
	telcasa 		= models.CharField(null=True, max_length=10)
	movil_id		= models.CharField(null=True, max_length=10)
	rfc				= models.CharField(null=True, max_length=20)
	nomFiscal		= models.CharField(null=True, max_length=50)
	dirFiscal		= models.CharField(null=True, max_length=50)
	concepto		= models.CharField(null=True, max_length=10)
	importe			= models.DecimalField(max_digits=10, decimal_places=2)
	status			= models.BooleanField(default=True)

	def __unicode__(self):
		return self.nombre







