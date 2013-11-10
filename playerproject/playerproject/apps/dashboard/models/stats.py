import time

from datetime import datetime, timedelta
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

from playerproject.libs.model.models import BaseModel


class PPPlayerStats (BaseModel):
    POSITION_NOT_SPECIFIED = 'not_specified'

    class Meta:
        app_label = 'dashboard'


class PPHockeyPlayerStats (PPPlayerStats): 
    POSITION_ANY = 'any'   
    POSITION_ANY_OFFENSE = 'any_forward'
    POSITION_ANY_DEFENSE = 'any_defense'

    POSITION_CHOICES = (
        (POSITION_ANY, 'Any'),
        (POSITION_ANY_OFFENSE, 'Offense'),
        (POSITION_ANY_DEFENSE, 'Defense')
    )

    position = models.CharField(
        max_length=30,
        choices=POSITION_CHOICES,
        default=PPPlayerStats.POSITION_NOT_SPECIFIED)
    
    goals = models.PositiveIntegerField(default=0)
    assists = models.PositiveIntegerField(default=0)
    points = models.PositiveIntegerField(default=0)

    class Meta:
        app_label = 'dashboard'

