from django.contrib.auth import get_user_model
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(
        to=get_user_model(), on_delete=models.CASCADE, primary_key=True, related_name="profile"
    )
    t_user_id = models.IntegerField("Telegram user id", blank=True, null=True)
    t_username = models.CharField("Telegram username", max_length=150, blank=True, null=True)
    photo = models.ImageField(
        default="/empty_avatar.png",
        null=True,
        blank=True,
        upload_to="profiles_avatars/%Y/%m/%d/",
        verbose_name="Avatar",
    )

    # date_created = models.DateTimeField(auto_now=True, null=True, editable=False, verbose_name="Modified date")

    # email = models.EmailField(_("Email address"), null=True, unique=True)
    # first_name = models.CharField(_("First name"), max_length=150, blank=True)
    # last_name = models.CharField(_("Last name"), max_length=150, blank=True)
    # address = models.CharField(max_length=255, blank=True, null=True, verbose_name="Address")
