from django.contrib import admin
from django.urls import include
from django.urls import path

from .views import UserView, CurrentUserView, ChangePasswordView


urlpatterns = [
    path("", UserView.as_view(), name="user"),
    path("/password", ChangePasswordView.as_view(), name="password"),
]
