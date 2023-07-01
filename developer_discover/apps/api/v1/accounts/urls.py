from django.contrib import admin
from django.urls import include
from django.urls import path

from .views import GithubSocialLoginView, GithubCallBackView, UserDestroyView, UserSignUpView, UserSignInView
from .views import UserEmailConfirmView, UserPasswordResetView


urlpatterns = [
    path("signup", UserSignUpView.as_view(), name="sign-up"),
    path("signin", UserSignInView.as_view(), name="sign-in"),
    path("email-check", UserEmailConfirmView.as_view(), name="email-confirm"),
    path("reset-password", UserPasswordResetView.as_view(), name="reset-password"),
    path("withdrawal", UserDestroyView.as_view(), name="withdrawal"),
    # path("", include("dj_rest_auth.urls")),
    # path("login/github", GithubSocialLoginView.as_view(), name="github-login"),
    # path("login/github/callback", GithubCallBackView.as_view(), name="github-callback"),
]
