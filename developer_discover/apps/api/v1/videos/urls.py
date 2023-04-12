from django.contrib import admin
from django.urls import include
from django.urls import path

from .views import VideoListView


urlpatterns = [
    path("current", VideoListView.as_view(), name="list"),
]
