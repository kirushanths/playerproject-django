from django import forms
from django.utils.translation import ugettext_lazy as _

from playerproject.apps.dashboard.models import PPHockeyUserRecord, PPHockeyPlayerStats, PPHockeyGoalieStats, PPHockeySkaterStats
from playerproject.libs.fields import SubmitButtonField

class PPHockeyUserRecordForm(forms.ModelForm):
    class Meta:
        fields = ['first_name', 'last_name', 'position']
        model = PPHockeyUserRecord

class PPHockeySkaterStatsForm(forms.ModelForm):
    class Meta:
        model = PPHockeySkaterStats
        fields = [  'height_feet', 
                    'height_inches',
                    'shoots', 
                    'games_played', 
                    'penalty_minutes', 
                    'wins', 
                    'losses', 
                    'ties', 
                    'goals', 
                    'assists', 
                    'points', 
                    'plus_minus',]

class PPHockeyGoalieStatsForm(forms.ModelForm):
    class Meta:
        model = PPHockeyGoalieStats
        fields = [  'height_feet', 
                    'height_inches',
                    'games_played', 
                    'penalty_minutes', 
                    'wins', 
                    'losses', 
                    'ties',
                    'save_percentage', 
                    'saves', 
                    'goals_against', 
                    'goals_against_avg', 
                    'shots_on_goal', 
                    'shutouts',
                    'minutes',
                    'games_started']
    