from django.conf.urls import patterns, url
from my_app import views

urlspatterns = patterns('', 
	url(r'^$', views.index, name='index'),
)
