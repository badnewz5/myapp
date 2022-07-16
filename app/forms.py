from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils import timezone


class FormRegistration(UserCreationForm):
    emai = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class UserUpdate(ModelForm):
    emai = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username','email']