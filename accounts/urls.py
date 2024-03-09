from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.SignupInterfaceView.as_view(), name="signup"),
    path("dashboard/", views.DashboardView.as_view(), name="dashboard"),
    path("profile/", views.UserProfileView.as_view(), name="user_profile"),
    path(
        "profile/<int:pk>/",
        views.UserProfilePictureUpdateView.as_view(),
        name="user_profile_picture_update",
    ),
    path(
        "profile/edit/<int:pk>/",
        views.ProfileEditView.as_view(),
        name="user_profile_edit",
    ),
    path(
        "profile/manage_email/<int:pk>/",
        views.ManageEmailView.as_view(),
        name="manage_email",
    ),
    path(
        "profile/edit/timezone/<int:pk>/",
        views.TimezoneEditView.as_view(),
        name="user_timezone_edit",
    ),
]
