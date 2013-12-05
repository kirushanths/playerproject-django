from django import forms
from django.utils.translation import ugettext_lazy as _

from playerproject.apps.dashboard.models import PPHockeyUserRecord, PPHockeyPlayerStats
from playerproject.libs.fields import SubmitButtonField

class PPHockeyUserRecordForm(forms.ModelForm):
    class Meta:
        fields = ['first_name', 'last_name']
        model = PPHockeyUserRecord


class PPHockeyPlayerStatsForm(forms.ModelForm):
    class Meta:
        model = PPHockeyPlayerStats
        fields = [  'height_feet', 
                    'height_inches',
                    'position', 
                    'shoots', 
                    'games_played', 
                    'penalty_minutes', 
                    'wins', 
                    'losses', 
                    'ties', 
                    'goals', 
                    'assists', 
                    'points', 
                    'plus_minus', 
                    'save_percentage', 
                    'saves', 
                    'goals_against', 
                    'goals_against_avg', 
                    'shots_on_goal', 
                    'shutouts',
                    'minutes',
                    'games_started']