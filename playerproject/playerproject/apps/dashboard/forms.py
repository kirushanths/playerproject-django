from django import forms
from django.utils.translation import ugettext_lazy as _

from playerproject.apps.dashboard.models import PPHockeyUserRecord, PPHockeyPlayerStats, PPHockeyGoalieStats, PPHockeySkaterStats, PPUserNote
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
                    'shots_on_goal', 
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
                    'shutouts',
                    'minutes',
                    'games_started']
                    
class PPUserNoteForm(forms.ModelForm):
    class Meta:
        model = PPUserNote
        fields = [  'title',
                    'content',]