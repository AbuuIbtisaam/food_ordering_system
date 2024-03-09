from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView
from django.views.generic.edit import CreateView, UpdateView

from accounts.models import CustomUser
from .forms import (
    CustomUserChangeForm,
    CustomUserCreationForm,
    CustomUserProfileUpdateForm,
    ManageEmailForm,
    ProfilePicUpdateForm,
    TimezoneUpdateForm,
)
from django.contrib.auth.mixins import LoginRequiredMixin

# from debit_management.models import Debtors, Debts

from django.views import View
from django.conf import settings
from django.views.static import serve
import os


class SignupInterfaceView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")

    # To redirect to dashboard if user is already logged in
    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("dashboard")
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.profile_picture = self.request.FILES.get("profile_picture")
        return super().form_valid(form)


class ProfileEditView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = CustomUserProfileUpdateForm
    template_name = "user_profile_edit.html"
    success_url = reverse_lazy("user_profile")


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard.html"
    login_url = "login"

    


class UserProfileView(LoginRequiredMixin, TemplateView):
    model = CustomUser
    template_name = "user_profile.html"
    object_context_name = "user"


class UserProfilePictureUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    template_name = "user_profilePicUpdate.html"
    # fields = ["profile_picture"]
    form_class = ProfilePicUpdateForm
    success_url = reverse_lazy("user_profile")

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(pk=self.request.user.pk)


class ManageEmailView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    # fields = ["email"]
    form_class = ManageEmailForm
    template_name = "manage_email.html"
    success_url = reverse_lazy("user_profile")

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(pk=self.request.user.pk)


class ProtectedMediaView(LoginRequiredMixin, View):
    login_url = "/login/"  # Set the URL to redirect non-authenticated users

    def get(self, request, *args, **kwargs):
        path = kwargs["path"]
        media_root = settings.MEDIA_ROOT
        file_path = os.path.join(media_root, path)

        if not os.path.exists(file_path):
            raise Http404
        if (
            not request.user.is_authenticated
            or not request.user.profile_picture.name.endswith(path)
        ):
            raise Http404

        return serve(request, path, document_root=media_root)


class TimezoneEditView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = TimezoneUpdateForm
    template_name = "user_timezone_edit.html"
    success_url = reverse_lazy("user_profile")

