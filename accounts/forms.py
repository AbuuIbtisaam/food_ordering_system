from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django import forms
from django.core.exceptions import ValidationError
from django.utils.timezone import datetime


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "date_of_birth",
            "profile_picture",
            # "time_zone",
        )
        widgets = {"date_of_birth": forms.DateInput(attrs={"type": "date"})}


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "date_of_birth",
            "profile_picture",
            # "time_zone",
        )


class CustomUserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = (
            "first_name",
            "last_name",
            "phone_number",
            "date_of_birth",
        )
        widgets = {"date_of_birth": forms.DateInput(attrs={"type": "date"})}

        def clean_date_of_birth(self):
            date_of_birth = self.cleaned_data["date_of_birth"]
            if date_of_birth >= datetime.date.today():
                raise ValidationError("Date of birth must be in the past.")
            return date_of_birth


class ManageEmailForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = [
            "email",
        ]
        widgets = {"email": forms.EmailInput()}


class ProfilePicUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = [
            "profile_picture",
        ]

    def clean(self):
        cleaned_data = super().clean()
        profile_picture = cleaned_data.get("profile_picture")

        if not profile_picture and not self.instance.profile_picture:
            self.add_error("profile_picture", "Profile picture is required.")
        elif profile_picture == self.instance.profile_picture:
            self.add_error("profile_picture", "Profile picture is required.")
        # return cleaned_data


class TimezoneUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ("time_zone",)
        labels = {"time_zone": "Timezone"}
