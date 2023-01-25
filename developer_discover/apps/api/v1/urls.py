from django.contrib import admin
from django.urls import include
from django.urls import path


urlpatterns = [
    path("users/", include("apps.api.v1.users.urls")),
]
