from django.forms import ModelForm
from django import forms
from django.db import models
from achievement.models import *

class AddContributionForm(ModelForm):
    bug_id = forms.IntegerField(
        required=True,
        label='bug_id',
        widget=forms.TextInput(
            attrs={'placeholder':'Bug ID/Ticket'}
        )
    )
    org_name=forms.CharField(
         required=True,
         label='Organisation Name',
         widget=forms.TextInput(
            attrs={'placeholder': 'Organisation Name'}
         )
    )
    bug_url=forms.CharField(
         required=True,
         label='Bug URL',
         widget=forms.TextInput(
            attrs={'placeholder': 'URL'}
         )
    )
    bug_description=forms.CharField(
         required=True,
         label='Description',
         widget=forms.Textarea(
            attrs={'placeholder': 'Description of Bug', \
            'cols': 20, 'rows': 5}
         )
    )
    class Meta:
		model = Contribution
		exclude = ['username', 'achievement_id',]
