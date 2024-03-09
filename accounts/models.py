import pytz as pytz
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.forms import ValidationError
from datetime import date, timedelta


class CustomUser(AbstractUser):
    date_of_birth = models.DateField()
    phone_regex = RegexValidator(
        regex=r"^\+?1?\d{9,15}$",
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed without space.",
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=16)
    profile_picture = models.ImageField(
        upload_to="images/",
        null=True,
        blank=True,
        help_text="",
    )
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)

    password = models.CharField(
        max_length=150,
        help_text="Required",
    )
    # To manage local timezones
    timezones = [(tz, tz) for tz in pytz.all_timezones]
    time_zone = models.CharField(max_length=100, choices=timezones, default="UTC")

    def clean(self):
        min_date = date.today() - timedelta(days=13 * 365)  # 13 years ago
        date_of_birth = self.date_of_birth
        if date_of_birth is not None and date_of_birth >= date.today():
            raise ValidationError("Date of birth must be in the past")

        elif date_of_birth is not None and date_of_birth > min_date:
            raise ValidationError("You must have at least 13 years old to register.")


# phonenumber field validation with country code selection
