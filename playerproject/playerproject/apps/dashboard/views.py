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
from playerproject.apps.dashboard.forms import PPUserRecordForm

def home(request):
    return render(request, 'dashboard/home.html')


def manager(request):
	playerrecords = PPUserRecord.objects.filter(recorded_by = request.user.id).order_by('time_modified')
	return render(request,'dashboard/records.html', {'records': playerrecords})


def manager_add(request):
    if request.POST:
        form = PPUserRecordForm(request.POST)
        if form.is_valid():
            # commit=False means the form doesn't save at this time.
            # commit defaults to True which means it normally saves.
            item = form.save(commit=False)
            item.recorded_by = request.user
            item.save()
            #redirect
            return HttpResponseRedirect(reverse('dashboard_manager'))
        else:
            print('error')
            #failed
    else:
        form = PPUserRecordForm()

    return render(request, 'dashboard/recordadd.html', { 'form':form })
