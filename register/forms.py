from django.forms import ModelForm
from django import forms
from register.models import *

class LoginForm(forms.Form):
	username = forms.CharField(max_length=20)
        password = forms.CharField(widget=forms.PasswordInput)


class NewRegisterForm(ModelForm):
	class Meta:
		model = User_info


class ProfileForm(ModelForm):
	class Meta:
		model = User_info
		exclude = ['password']


class OtherProfileForm(ModelForm):
	class Meta:
		model = User_info
		exclude = ['username', 'password', 'contact']


class ChangePasswordForm(forms.Form):
	old_password = forms.CharField(max_length=20, widget=forms.PasswordInput)
	new_password = forms.CharField(max_length=20, widget=forms.PasswordInput)
	confirm_new_password = forms.CharField(max_length=20, widget=forms.PasswordInput)
