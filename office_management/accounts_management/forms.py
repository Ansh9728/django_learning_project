from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    FirstName = forms.CharField(max_length=100,)
    LastName = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['username', 'email', 'FirstName', 'LastName', 'password1', 'password2']