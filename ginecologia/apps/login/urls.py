from django.conf.urls.defaults import patterns,url

urlpatterns = patterns('ginecologia.apps.login.views',
			url(r'^$','login_view', name='vista_login'),
			url(r'^registro/$','registerView', name='vista_register'),
			url(r'^logout/$','logout_view', name='vista_logout'),

)