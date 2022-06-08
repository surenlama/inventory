from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.validators import MinLengthValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_(
            "Required. 5 - 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[username_validator, MinLengthValidator(5)],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )

