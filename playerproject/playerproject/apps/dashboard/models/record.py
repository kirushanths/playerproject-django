import time

from datetime import datetime, timedelta
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

from playerproject.libs.model.models import BaseModel
from playerproject.apps.accounts.models import PPUser, PPUserContactInfo
from playerproject.apps.dashboard.models.stats import PPHockeyPlayerStats, PPPlayerStats
from playerproject.apps.dashboard.models.note import PPUserNote

class PPUserRecord (BaseModel):
    first_name = models.CharField(_('first name'), max_length=50, null=True, blank=True)
    last_name = models.CharField(_('last name'), max_length=50, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)

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

    notes = models.ManyToManyField(
        PPUserNote,
        related_name='+'
    )

    class Meta:
        abstract = True
        app_label = 'dashboard'


class PPHockeyUserRecord(PPUserRecord):
     # Playing Position
    POSITION_ANY = 'any'   
    POSITION_ANY_OFFENSE = 'any_forward'
    POSITION_ANY_DEFENSE = 'any_defense'
    POSITION_GOALIE = 'G'

    POSITION_CHOICES = (
        (PPPlayerStats.POSITION_NOT_SPECIFIED, 'Unspecified'),
        (POSITION_ANY, 'Any'),
        (POSITION_ANY_OFFENSE, 'Offense'),
        (POSITION_ANY_DEFENSE, 'Defense'),
        (POSITION_GOALIE, 'Goalie'),
    )

    position = models.CharField(
        max_length=30,
        choices=POSITION_CHOICES,
        default=PPPlayerStats.POSITION_NOT_SPECIFIED)

    stats = models.ForeignKey(
        PPHockeyPlayerStats,
        related_name='+',
        null=True,
        blank=True
    )

    # Check if position is goalie
    def is_goalie(self): 
        return self.position == self.POSITION_GOALIE

    class Meta:
        app_label = 'dashboard'

