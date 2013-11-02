from django.shortcuts import render
from django.contrib.auth import (
    authenticate as django_auth,
    login as django_login,
    logout as django_logout
)
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from .models import DZUser
from .forms import DZUserModelForm, DZUserLoginForm

def login(request):
    if request.POST:
        login_form = DZUserLoginForm(data=request.POST)

        if login_form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = django_auth(username=username, password=password)

            if user is not None:
                if user.is_active:
                    django_login(request, user)

                    if user.is_developer():
                        return HttpResponseRedirect(reverse('developer_home'))
                    else:
                        return HttpResponseRedirect(reverse('dashboard_home'))

                else:
                    # Return a 'disabled account' error message
                    print('asdf')
                    pass
            else:
                # Return an 'invalid login' error message.
                print('asdf')
    else:
        login_form = DZUserLoginForm()

    return render(request, 'accounts/login.html', {'form': login_form})


def logout(request):
    django_logout(request)
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('account_login'))


def register(request):
    if request.POST:
        user_form = DZUserModelForm(request.POST)
        if user_form.is_valid():
            # commit=False means the form doesn't save at this time.
            # commit defaults to True which means it normally saves.
            user = user_form.save(commit=False)
            user.save()
            #redirect
            return HttpResponseRedirect(reverse('dashboard_home'))
        else:
            print('error')
            #failed
    else:
        user_form = DZUserModelForm()

    return render(request, 'accounts/register.html', {'user_form': user_form})


def developer_register(request):
    if request.POST:
        user_form = DZUserModelForm(request.POST)
        if user_form.is_valid():
            # commit=False means the form doesn't save at this time.
            # commit defaults to True which means it normally saves.
            user = user_form.save(commit=False)
            user.role = DZUser.ROLE_DEVELOPER
            user.save()
            #redirect
            return HttpResponseRedirect(reverse('dashboard_home'))
        else:
            print('error')
            #failed
    else:
        user_form = DZUserModelForm()

    return render(request, 'accounts/register_developer.html', {'user_form': user_form})

