from django.conf.urls import patterns, url, include
from django.contrib import auth

urlpatterns = patterns('apps.dashboard.developer.views',
	url(r'^$', 'home', name='developer_home'),
	url(r'^manager/', 'manager', name='developer_manager'),
    url(r'^upload/confirm/', 'upload_confirm', name='developer_upload_confirm'),
    url(r'^upload/', 'upload', name='developer_upload'),
    
    url(r'^site/(?P<site_id>\d+)/preview$', 'site_preview', name='developer_site_preview'),
    url(r'^site/(?P<site_id>\d+)/$', 'site_overview', name='developer_site_overview'),
)