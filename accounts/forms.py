from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    # date_of_birth = forms.DateTimeField()
    class Meta:
        model = User
        fields = ('username', 'email', 'password1')


class LoginForm(forms.Form):
    """user login form"""
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
