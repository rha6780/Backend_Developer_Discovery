from django.contrib import admin
from django.urls import include
from django.urls import path
from . import views

urlpatterns = [
    path("password-change", views.password_change, name="password_change"),
    path("email-change", views.email_change, name="email_change"),
]
