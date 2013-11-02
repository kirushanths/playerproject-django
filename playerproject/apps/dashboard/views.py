from django.shortcuts import render, get_object_or_404
from django.contrib.auth import (
    authenticate as django_auth,
    login as django_login,
    logout as django_logout
)
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import (
    HttpResponse,
    HttpResponseRedirect
)

from dazzle.apps.accounts.models import DZUser
from dazzle.apps.dashboard.models import DZSite, DZTemplate

@login_required
def home(request):
    return HttpResponseRedirect(reverse('dashboard_manager'))


@login_required
def manager(request):

    if request.user.is_developer():
        return HttpResponseRedirect(reverse('developer_home'))

    user_sites = request.user.sites.all()

    context = {
        'sites': user_sites
    }

    return render(request, 'dashboard/manager.html', dictionary=context)


@login_required
def library(request):

    templates = DZTemplate.objects.all()

    context = {
        'templates': templates
    }

    return render(request, 'dashboard/library.html', dictionary=context)


@login_required
def site_overview(request, site_id):
    site = get_object_or_404(DZSite, pk=site_id)

    context = {
        'site' : site
    }

    return render(request, 'dashboard/overview.html', dictionary=context)



