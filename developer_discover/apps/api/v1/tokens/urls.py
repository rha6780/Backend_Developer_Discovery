from django.contrib import admin
from django.urls import include
from django.urls import path

from .views import TokenView

# from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token


urlpatterns = [
    path("", TokenView.as_view(), name="token"),
    path("api/token/", obtain_jwt_token),
    path("api/token/verify/", verify_jwt_token),
    path("api/token/refresh/", refresh_jwt_token),
]
