from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeInterfaceView.as_view(), name="home"),
]