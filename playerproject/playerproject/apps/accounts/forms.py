from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm,
    UserChangeForm
)

from .models import DZUser

from dazzle.libs.fields import SubmitButtonField

class DZUserLoginForm(AuthenticationForm):
    submit = SubmitButtonField(label="", initial=u"Sign In")


class DZQuickUserModelForm(UserCreationForm):
    """
    A form that creates a user, with no privileges, from the given email and
    password.
    """
    error_messages = {
        'duplicate_email': _("A user with that email already exists.")
    }

    submit = SubmitButtonField(label="", initial=u"Sign Up")

    def __init__(self, *args, **kargs):
        super(DZQuickUserModelForm, self).__init__(*args, **kargs)
        del self.fields['username']

    class Meta:
        fields = ('email',)
        model = DZUser

    def clean_email(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        email = self.cleaned_data["email"]
        try:
            DZUser._default_manager.get(email=email)
        except DZUser.DoesNotExist:
            return email
        raise forms.ValidationError(
            self.error_messages['duplicate_email'],
            code='duplicate_email',
        )


class DZUserModelForm(DZQuickUserModelForm):
    class Meta:
        fields = ('email', 'first_name', 'last_name',)
        model = DZUser


class DZUserChangeForm(UserChangeForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """

    submit = SubmitButtonField(label="", initial=u"Update")

    def __init__(self, *args, **kargs):
        super(DZUserChangeForm, self).__init__(*args, **kargs)
        del self.fields['username']

    class Meta:
        model = DZUser
        fields = ('email', 'first_name', 'last_name',)


