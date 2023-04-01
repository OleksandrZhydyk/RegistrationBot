import json
import os

from django.contrib.auth import get_user_model, authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import RegistrationForm, ProfileForm, LoginForm
from . models import Profile


BOT_URL = os.getenv('BOT_URL')


def index(request):
    return render(
        request,
        template_name="accounts/registration.html",
        context={"title": "Registration",
                 "bot_url": BOT_URL,
                 },
    )


def check_user_exist(request, t_user_id):
    user = Profile.objects.filter(t_user_id=t_user_id)
    if user:
        return JsonResponse({'user_exist': True})
    return JsonResponse({'user_exist': False})


def check_username_exist(request, username):
    user = get_user_model().objects.filter(username=username)
    if user:
        return JsonResponse({'username_exist': True})
    return JsonResponse({'username_exist': False})


def registration(request):
    if request.method == "POST":
        data = json.loads(request.body.decode())
        user_form = RegistrationForm(data)
        if user_form.is_valid():
            user = user_form.save()
            return JsonResponse({'registration': True, 'user': user.username})
        else:
            return JsonResponse({'registration': False})


def update_profile(request, username):
    if request.method == "POST":
        user = get_user_model().objects.get(username=username)
        profile = Profile.objects.get(user=user)

        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return JsonResponse({'profile_update': True})
        return JsonResponse({'profile_update': False})


def login_user(request):
    if request.method == "POST":
        form = LoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user:
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                return redirect("profile", username)
            else:
                return render(
                    request=request,
                    template_name="accounts/login.html",
                    context={"form": form, "message": "Invalid username or password"},
                )
        else:
            return render(
                request=request,
                template_name="accounts/login.html",
                context={"form": form, "message": "Invalid username or password"},
            )
    form = LoginForm()
    return render(request=request, template_name="accounts/login.html", context={"form": form})


@login_required
def get_profile(request, username):
    user = get_user_model().objects.get(username=username)
    if request.user.id == user.id:
        profile = Profile.objects.get(user=user)
        return render(
            request,
            template_name="accounts/profile.html",
            context={"title": "Profile",
                     "profile": profile,
                     },
        )
    return render(request, template_name="accounts/forbidden.html")
