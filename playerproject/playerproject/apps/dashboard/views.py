from django.shortcuts import render
from django.contrib.auth import (
    authenticate as django_auth,
    login as django_login,
    logout as django_logout
)
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from playerproject.apps.accounts.models import PPUser
from playerproject.apps.dashboard.models import (
    PPUserRecord,
    PPHockeyPlayerStats,
    PPPlayerStats
)

def home(request):
    return render(request, 'dashboard/home.html')


def manager(request):
	playerrecords = PPUserRecord.objects.filter(recorded_by = request.user.id).order_by('time_modified').order_by('time_modified')
	return render(request,'dashboard/records.html', {'records': playerrecords})


def manager_add(request):
    pass