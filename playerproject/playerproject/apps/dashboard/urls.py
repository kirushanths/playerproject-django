from django.conf.urls import patterns, url, include
from django.contrib import auth

urlpatterns = patterns('apps.dashboard.views',
    url(r'^home/$', 'home', name="dashboard_home"),

    url(r'^manager/$', 'manager', name="dashboard_manager"),
    url(r'^manager/add/$', 'manager_add', name="dashboard_manager_add"),

    url(r'^player/(?P<player_id>\d+)/$', 'player', name='dashboard_player'),
    url(r'^player/stats/(?P<player_id>\d+)/$', 'player_stats_update', name='dashboard_player_stats_update'),
)