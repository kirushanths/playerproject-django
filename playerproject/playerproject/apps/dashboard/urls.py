from django.conf.urls import patterns, url, include
from django.contrib import auth

urlpatterns = patterns('apps.dashboard.views',
    url(r'^home/$', 'home', name="dashboard_home"),
    url(r'^manager/$', 'manager', name="dashboard_manager"),
    url(r'^manager/add/$', 'manager_add', name="dashboard_manager_add"),
)