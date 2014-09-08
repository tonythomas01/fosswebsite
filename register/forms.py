from django.forms import ModelForm
from django import forms
from django.db import models
from django.forms.fields import DateField, ChoiceField, MultipleChoiceField
from django.forms.widgets import RadioSelect, CheckboxSelectMultiple
from captcha.fields import ReCaptchaField
import re

#from django.core import Validator
from django.shortcuts import get_object_or_404
from register.models import User_info

GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'))
ROLE_CHOICES = (('S', 'Student'), ('M', 'Mentor'), ('B', 'Both'))
GOAL_CHOICES = (('startup', 'startup'), ('higher_studies', 'Higher Studies'), ('job', 'Job'), ('other', 'Others'))


#custom functions
def check_alpha(name):
    """
    Checks for the only presence of alphabets
    """
    if re.match("^[a-za-z ]*$",name):
        return true
    else:
        return false


def user_exists(email_):
    """
    Checks if a user exists or not
    """
    if User_info.objects.all().filter(email=email_):
        return true
    else:
        return false


class LoginForm(forms.Form):
    username=forms.CharField(
        required=True,
        max_length=100,
        label='Username', 
        widget=forms.TextInput(
            attrs={'placeholder': 'Username'}
        )
    )

    password=forms.CharField(
        required=True,
        max_length=100,
        label='Password',
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Password'}
        )
    )

    def clean_repass(self):
        password = self.cleaned_data['password']
        re_password = self.cleaned_data['repass']
        if password == re_password:
            return password
        else:
            raise forms.ValidationError("Passwords don't match")


class NewRegisterForm(ModelForm):
    """
    Registration form
    """
    firstname=forms.CharField(
         required=True,
         label='First Name', 
         widget=forms.TextInput(
            attrs={'placeholder': 'Firstname'}
         )
    )

    lastname=forms.CharField(
         required=True,
         label='Last Name', 
         widget=forms.TextInput(
            attrs={'placeholder': 'Lastname'}
         )
    )

    gender=forms.CharField(
        required=True,
        label='Gender', 
        widget=forms.Select(
            choices=GENDER_CHOICES, 
            attrs={'placeholder': 'Gender'}
            )
    )

    contact = forms.IntegerField(
        required=True,
        label='Phone number', 
        widget=forms.TextInput(
            attrs={'placeholder':'Phone Number'}
        )
    )

    role=forms.CharField(
        required=True,
        label='Role', 
        widget=forms.Select(
            choices=ROLE_CHOICES, 
            attrs={'placeholder': 'Role'}, 
        )
    )

    interest = forms.CharField(
        required=True,
        label='Interests', 
        widget=forms.TextInput(
            attrs={'placeholder':'Interests'}
        )
    )

    achieve = forms.CharField(
        required=True,
        label='Achievement', 
        widget=forms.TextInput(
            attrs={'placeholder':'Achievements'}
        )
    )

    expertise = forms.CharField(
        required=True,
        label='Expertise', 
        widget=forms.TextInput(
            attrs={'placeholder':'Expertize'}
        )
    )

    goal=forms.CharField(
        required=True,
        label='Goal', 
        widget=forms.Select(
            choices=GOAL_CHOICES, 
            attrs={'placeholder': 'Goal'}, 
        )
    )
    
    email=forms.EmailField(
        required=True,
        label='Email', 
        widget=forms.TextInput(
            attrs={'placeholder': 'Email Address'}
        )
    )

    username=forms.CharField(
        required=True,
        label='Username', 
        widget=forms.TextInput(
            attrs={'placeholder': 'Username'}
        )
    )

    password=forms.CharField(
        required=True,
        max_length=100,
        label='Password',
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Password'}
        )
    )

    repass = forms.CharField(
        max_length=100,
        required=True,
        label='Re-enter password',
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Re Enter Your Password'}
        ),
    )

    captcha = ReCaptchaField(
        attrs={'theme':'clean'}
    )

    class Meta:
        model = User_info

    def clean_name(self):
        """
        Checks for non-alphabets in the username.
        Raises an error if found
        """
        username = self.cleaned_data['username']
        if check_alpha(username):
            return username
        else:
            raise forms.ValidationError("Please enter only alphabets")

    def clean_repass(self):
        """
        If passwords doesn't match, both the password
        fields will be cleard by raising an error
        """
        password = self.cleaned_data['password']
        re_password = self.cleaned_data['repass']
        if password == re_password:
            return password
        else:
            raise forms.ValidationError("Passwords don't match")


class ChangePasswordForm(forms.Form):
    """
    Password changer form
    """
    old_password=forms.CharField(
        required=True,
        max_length=100,
        label='Current Password',
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Current Password'}
        )
    )

    new_password = forms.CharField(
        required=True,
        max_length=100,
        label='New Password',
        widget=forms.PasswordInput(
            attrs={'placeholder': 'New Password'} 
        )
    )

    confirm_new_password = forms.CharField(
        max_length=100, 
        required=True,
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Confirm new password'} 
        )
    )

    def clean_repass(self):
        """
        If passwords doesn't match, both the password
        fields will be cleard by raising an error
        """
        password = self.cleaned_data['new_password']
        re_password = self.cleaned_data['confirm_new_password']
        if password == re_password:
            return password
        else:
            raise forms.ValidationError("Passwords don't match")
