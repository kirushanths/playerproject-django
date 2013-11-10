import time

from datetime import datetime, timedelta
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

from playerproject.libs.model.models import BaseModel

class PPUserContactInfo (BaseModel):

    phone_number = models.CharField(_('phone number'), max_length=50, null=True, blank=True)
    
    # TODO Address

    class Meta:
        app_label = 'accounts'

