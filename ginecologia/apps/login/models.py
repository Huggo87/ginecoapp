from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
	def url(self,filename):
		ruta = "MultimediaData/User/%s/%s"%(self.user.username,filename)
		return ruta

	user 	 = models.OneToOneField(User)
	telefono = models.CharField(max_length=20)
	photo 	 = models.ImageField(upload_to=url)

	def __unicode__(self):
		return self.user.username