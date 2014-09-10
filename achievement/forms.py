from django.forms import ModelForm
from bootstrap3_datetime.widgets import DateTimePicker
from django import forms
from django.db import models
from achievement.models import *

class AddContributionForm(ModelForm):
    """
    Form to add open source Contribution
    """
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


class AddArticleForm(ModelForm):
    """
    Form to add information about articles
    """
    article_id = forms.IntegerField(
        required=True,
        label='Article ID',
        widget=forms.TextInput(
            attrs={'placeholder':'Article ID'}
        )
    )

    title=forms.CharField(
         required=True,
         label='Title',
         widget=forms.TextInput(
            attrs={'placeholder': 'Title of the article'}
         )
    )

    area=forms.CharField(
         required=True,
         label='Area',
         widget=forms.TextInput(
            attrs={'placeholder': 'Area of the article'}
         )
    )

    magazine_name=forms.CharField(
         required=True,
         label='Magazine',
         widget=forms.TextInput(
            attrs={'placeholder': 'URL'}
         )
    )

    publication_date=forms.DateField(
        required=True,
        widget=DateTimePicker(
            options={"pickTime": False, 
                "format":"YYYY-MM-DD"},
            attrs={'placeholder': 'Published Date (DD-MM-YYYY)'}
        )
    )

    class Meta:
        model = Article
        exclude = ['username', 'achievement_id',]
