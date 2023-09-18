from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser


class RegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser  # Replace with your custom user model
        fields = ['username', 'password1', 'password2']  # Include other fields if needed


class LoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser  # Replace with your custom user model
        fields = ['username', 'password']  # Include other fields if needed


class RegistrationForm(UserCreationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'placeholder': 'Enter your username'}))
    # Customize other fields if needed

    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2']
