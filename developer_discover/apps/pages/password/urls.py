from django.contrib import admin
from django.urls import include
from django.urls import path
from . import views

urlpatterns = [
    path("<str:token>", views.token, name="token"),
    path("email-check", views.email_check, name="email-check"),
]
