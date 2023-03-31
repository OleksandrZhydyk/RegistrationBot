from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from . models import Profile


class RegistrationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ("username", "password1", "password2")


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("t_user_id", "t_username", "photo")


class LoginForm(AuthenticationForm):
    class Meta:
        model = get_user_model()
        fields = ("username", "password")
