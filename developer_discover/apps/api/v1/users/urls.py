from django.contrib import admin
from django.urls import include
from django.urls import path

from .views import ChangeEmailView, CurrentUserView


urlpatterns = [
    path("current", CurrentUserView.as_view(), name="current"),
    path("email", ChangeEmailView.as_view(), name="email"),
]
