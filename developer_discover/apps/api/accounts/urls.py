from django.contrib import admin
from django.urls import include
from django.urls import path

from .views import GithubSocialLoginView


urlpatterns = [
    path("login/github", GithubSocialLoginView.as_view(), name="github-login"),
    path("login/github/callback", GithubSocialLoginView.as_view(), name="github-callback"),
    path("", include("dj_rest_auth.urls")),
]
