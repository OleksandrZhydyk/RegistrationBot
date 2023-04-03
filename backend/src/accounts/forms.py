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
        fields = ("t_user_id", "t_username", "t_first_name", "photo")


class LoginForm(AuthenticationForm):
    class Meta:
        model = get_user_model()
        fields = ("username", "password")

    username = forms.CharField(
        label="", widget=forms.TextInput(attrs={"class": "form-control form-control",
                                                "placeholder": "username", "type": "text"})
    )
    password = forms.CharField(
        label="",
        widget=forms.PasswordInput(attrs={"class": "form-control form-control", "placeholder": "password"}),
    )
