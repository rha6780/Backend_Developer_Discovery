from django.contrib import admin
from django.urls import include
from django.urls import path

from .views import GithubSocialLoginView, GithubCallBackView, UserSignUpView, UserSignInView


urlpatterns = [
    path("login/github", GithubSocialLoginView.as_view(), name="github-login"),
    path("login/github/callback", GithubCallBackView.as_view(), name="github-callback"),
    path("signup", UserSignUpView.as_view(), name="sign-up"),
    path("signin", UserSignInView.as_view(), name="sign-in"),
    path("", include("dj_rest_auth.urls")),
]
