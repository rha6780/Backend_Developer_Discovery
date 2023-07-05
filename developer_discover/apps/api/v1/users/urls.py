from django.contrib import admin
from django.urls import include
from django.urls import path

from .views import UserView, ChangePasswordView, UserImageView


urlpatterns = [
    path("", UserView.as_view(), name="user"),
    path("/password", ChangePasswordView.as_view(), name="password"),
    path("/image", UserImageView.as_view(), name="image"),
]
