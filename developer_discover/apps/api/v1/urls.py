from django.contrib import admin
from django.urls import include
from django.urls import path

urlpatterns = [
    path("tokens/", include("apps.api.v1.tokens.urls")),
    path("users/", include("apps.api.v1.users.urls")),
    path("posts/", include("apps.api.v1.posts.urls")),
]
