# Create your views here.
from django.shortcuts import render
from django.contrib.auth import (
    authenticate as django_auth,
    login as django_login,
    logout as django_logout
)
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

def home(request):
    return render(request, 'corporate/home.html')