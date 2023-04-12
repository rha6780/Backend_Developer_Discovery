from django.contrib import admin
from django.urls import include
from django.urls import path

from .views import VideoListView


urlpatterns = [
    path("list", VideoListView.as_view(), name="list"),
]
