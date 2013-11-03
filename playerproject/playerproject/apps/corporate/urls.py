from django.conf.urls import patterns, url, include
from django.contrib import auth

urlpatterns = patterns('apps.corporate.views',
	url(r'^$', 'home', name='corporate_home')
)
