from django.contrib import admin
from django.urls import include
from django.urls import path

from .views import UserView


urlpatterns = [
    path("current", UserView.as_view(), name="current"),
]
