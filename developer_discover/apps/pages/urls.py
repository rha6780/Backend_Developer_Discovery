from django.contrib import admin
from django.urls import include
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("signin", views.signin, name="signin"),
    path("signup", views.signup, name="signin"),
    path("profile", views.profile, name="profile"),
    # path("withdrawal", views.withdrawal, name="withdrawal"),
    path("post/", include("apps.pages.post.urls")),
    path("accounts/", include("apps.pages.accounts.urls")),
    path("password/", include("apps.pages.password.urls")),
]
