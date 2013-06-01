from django.conf.urls.defaults import patterns,url

urlpatterns = patterns('ginecologia.apps.paciente.views',
			url(r'^altapaciente/$','alta_paciente_view',name='vista_nuevo_pacinete'),
			url(r'^dashboard/$','dashboard_view',name='vista_dashboard'),
)