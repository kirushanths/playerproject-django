import time

from datetime import datetime, timedelta
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

from playerproject.libs.model.models import BaseModel
from playerproject.apps.accounts.models import PPUser, PPUserContactInfo

class PPUserRecord (BaseModel):
    first_name = models.CharField(_('first name'), max_length=50, null=True, blank=True)
    last_name = models.CharField(_('last name'), max_length=50, null=True, blank=True)



    contact_info = models.ForeignKey(
        PPUserContactInfo,
        related_name='+',
        null=True,
        blank=True
    )

    recorded_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='+',
        null=True,
        blank=True
    )

    class Meta:
        app_label = 'dashboard'

