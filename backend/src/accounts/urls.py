from django.urls import path
from . views import index, check_user_exist, \
    check_username_exist, registration, update_profile, get_profile, login_user
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path("", index, name="index"),
    path("user_exist/<int:t_user_id>", check_user_exist),
    path("username_exist/<str:username>", check_username_exist),
    path("register", csrf_exempt(registration)),
    path("update_profile/<str:username>", csrf_exempt(update_profile)),
    path("login", login_user),
    path("profile/<str:username>", get_profile, name="profile")
]
