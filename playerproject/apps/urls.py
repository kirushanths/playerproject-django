from django.conf.urls import patterns, url, include
from django.contrib import auth

urlpatterns = patterns('',
	url(r'', include('apps.corporate.urls')),
	url(r'^accounts/', include('apps.accounts.urls')),
	url(r'^dashboard/', include('apps.dashboard.urls')),

    url(r'upload/(.+)$', include('apps.engine.urls')),
    url(r'update/(.+)$', include('apps.engine.urls')),
    url(r'^', include('apps.engine.urls'))
)
