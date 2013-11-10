from django.conf.urls import patterns, url, include
from django.contrib import auth

urlpatterns = patterns('apps.accounts.views',
	url(r'^login/$', 'login', name="account_login"),
	url(r'^logout/$', 'logout', name="account_logout"),
	url(r'^register/$', 'register', name="account_register"),
    url(r'^register/recruiter/$', 'recruit_register', name="account_register_recruit"),
)

urlpatterns += patterns('',
)