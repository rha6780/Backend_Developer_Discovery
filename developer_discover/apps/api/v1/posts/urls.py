from django.contrib import admin
from django.urls import include
from django.urls import path

from .views import PostListView


urlpatterns = [
    path("list", PostListView.as_view(), name="list"),
]
