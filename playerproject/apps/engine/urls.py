from django.conf.urls import patterns, url

urlpatterns = patterns('apps.engine.views',
	url(r'update/(?P<template_name>.+)/$', 'update', name='update'),
	url(r'upload/(?P<template_name>.+)/$', 'upload', name='upload'),
	url(r'(?P<template_name>.+)/$', 'convert', name='convert'),

)
