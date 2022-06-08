from tkinter import Label
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class SignUpForm(UserCreationForm):
    password1 = forms.CharField(
        label="password (again)", widget=forms.PasswordInput())
    password2 = forms.CharField(
        label="Confirm Password (again)", widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password1', 'password2']
        labels = {'email': 'Email'}
