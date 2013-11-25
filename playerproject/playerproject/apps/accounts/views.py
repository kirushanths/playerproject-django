from django.shortcuts import render
from django.contrib.auth import (
    REDIRECT_FIELD_NAME,
    authenticate as django_auth,
    login as django_login,
    logout as django_logout
)
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from django.views.decorators.debug import sensitive_post_parameters
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect

from django.utils.http import is_safe_url
from django.shortcuts import resolve_url

from playerproject import settings

from .models import PPUser
from .forms import PPUserModelForm, PPUserLoginForm

@sensitive_post_parameters()
@csrf_protect
@never_cache
def login(request, redirect_field_name=REDIRECT_FIELD_NAME):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('dashboard_home'))

    if request.POST:
        login_form = PPUserLoginForm(data=request.POST)

        if login_form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = django_auth(username=username, password=password)

            if user is not None:
                if user.is_active:
                    redirect_to = request.POST.get(redirect_field_name,
                                   request.GET.get(redirect_field_name, ''))

                    # Ensure the user-originating redirection url is safe.
                    if not is_safe_url(url=redirect_to, host=request.get_host()):
                        redirect_to = resolve_url(settings.LOGIN_REDIRECT_URL)

                    django_login(request, user)

                    return HttpResponseRedirect(redirect_to)

                else:
                    # Return a 'disabled account' error message
                    print('asdf')
                    pass
            else:
                # Return an 'invalid login' error message.
                print('asdf')
    else:
        login_form = PPUserLoginForm()

    return render(request, 'accounts/login.html', {'form': login_form})


def logout(request):
    django_logout(request)
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('account_login'))


def register(request):
    if request.POST:
        user_form = PPUserModelForm(request.POST)
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
        user_form = PPUserModelForm()

    return render(request, 'accounts/register.html', {'user_form': user_form})


def recruit_register(request):
    if request.POST:
        user_form = PPUserModelForm(request.POST)
        if user_form.is_valid():
            # commit=False means the form doesn't save at this time.
            # commit defaults to True which means it normally saves.
            user = user_form.save(commit=False)
            user.role = PPUser.ROLE_RECRUITER
            user.save()
            #redirect
            return HttpResponseRedirect(reverse('dashboard_home'))
        else:
            print('error')
            #failed
    else:
        user_form = PPUserModelForm()

    return render(request, 'accounts/register_recruiter.html', {'user_form': user_form})

