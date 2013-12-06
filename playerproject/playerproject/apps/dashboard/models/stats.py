import time

from datetime import datetime, timedelta
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

from playerproject.libs.model.models import BaseModel

class PPPlayerStats (BaseModel):
    POSITION_NOT_SPECIFIED = 'not_specified'
    height_feet = models.PositiveIntegerField(null=True, blank=True)
    height_inches = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        abstract = True
        app_label = 'dashboard'


class PPHockeyPlayerStats (PPPlayerStats): 

    # Playing Position
    POSITION_ANY = 'any'   
    POSITION_ANY_OFFENSE = 'any_forward'
    POSITION_ANY_DEFENSE = 'any_defense'

    POSITION_CHOICES = (
        (PPPlayerStats.POSITION_NOT_SPECIFIED, 'Unspecified'),
        (POSITION_ANY, 'Any'),
        (POSITION_ANY_OFFENSE, 'Offense'),
        (POSITION_ANY_DEFENSE, 'Defense')
    )

    # Shooting Hand
    SHOOTS_POSITION_NOT_SPECIFIED = 'shoots_unspecified'
    SHOOTS_POSITION_LEFT = 'shoots_left'
    SHOOTS_POSITION_RIGHT = 'shoots_right'

    SHOOTS_POSITION_CHOICES = (
        (SHOOTS_POSITION_NOT_SPECIFIED, 'Unspecified'),
        (SHOOTS_POSITION_LEFT, 'Shoots Left'),
        (SHOOTS_POSITION_RIGHT, 'Shoots Right'),
    )

    position = models.CharField(
        max_length=30,
        choices=POSITION_CHOICES,
        default=PPPlayerStats.POSITION_NOT_SPECIFIED)

    shoots = models.CharField(
        max_length=30,
        choices=SHOOTS_POSITION_CHOICES,
        default=SHOOTS_POSITION_NOT_SPECIFIED)
    
    games_played = models.PositiveIntegerField(default=0)
    penalty_minutes = models.PositiveIntegerField(default=0)

    # Record Stats
    wins = models.PositiveIntegerField(default=0)
    losses = models.PositiveIntegerField(default=0)
    ties = models.PositiveIntegerField(default=0)

    # Offensive Stats
    goals = models.PositiveIntegerField(default=0)
    assists = models.PositiveIntegerField(default=0)
    points = models.PositiveIntegerField(default=0)
    plus_minus = models.IntegerField(default=0)

    # Goalie Stats
    save_percentage = models.DecimalField(max_digits=5, decimal_places=4)
    saves = models.PositiveIntegerField(default=0)
    goals_against = models.PositiveIntegerField(default=0)
    goals_against_avg = models.DecimalField(max_digits=6, decimal_places=3)
    shots_on_goal = models.PositiveIntegerField(default=0)
    shutouts = models.PositiveIntegerField(default=0)
    minutes = models.PositiveIntegerField(default=0)
    games_started = models.PositiveIntegerField(default=0)


    class Meta:
        app_label = 'dashboard'

