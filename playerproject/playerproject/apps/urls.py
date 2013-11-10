from django.conf.urls import patterns, url, include
from django.contrib import auth

urlpatterns = patterns('',
	url(r'', include('apps.corporate.urls')),
	url(r'^accounts/', include('apps.accounts.urls')),
    url(r'^dashboard/', include('apps.dashboard.urls')),
)
