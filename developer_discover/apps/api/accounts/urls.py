from django.contrib import admin
from django.urls import include
from django.urls import path

from .views import GithubSocialLoginView, GithubCallBackView, UserSignUpView, UserSignInView
from .views import UserPasswordView, UserPasswordConfirmView


urlpatterns = [
    path("login/github", GithubSocialLoginView.as_view(), name="github-login"),
    path("login/github/callback", GithubCallBackView.as_view(), name="github-callback"),
    path("signup", UserSignUpView.as_view(), name="sign-up"),
    path("signin", UserSignInView.as_view(), name="sign-in"),
    path("reset-password", UserPasswordView.as_view(), name="reset-password"),
    path("reset-password/<str:uid64>/<str:token>/", UserPasswordConfirmView.as_view(), name="reset-password"),
    path("", include("dj_rest_auth.urls")),
]
# /<str:uidb64>/<str:token>/
