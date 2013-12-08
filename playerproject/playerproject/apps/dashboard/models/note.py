import time

from datetime import datetime, timedelta
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

from playerproject.libs.model.models import BaseModel

class PPUserNote (BaseModel):
    content = models.TextField(_('content'))
    title = models.CharField(_('title'), max_length=50)

    class Meta:
        app_label = 'dashboard'