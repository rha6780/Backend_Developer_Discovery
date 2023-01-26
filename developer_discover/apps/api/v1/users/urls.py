from django.contrib import admin
from django.urls import include
from django.urls import path

from .views import CurrentUserView


urlpatterns = [
    path("current", CurrentUserView.as_view(), name="current"),
]
