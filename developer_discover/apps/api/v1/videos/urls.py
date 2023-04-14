from django.contrib import admin
from django.urls import include
from django.urls import path

from .views import VideoListView, VideoUpdateView


urlpatterns = [
    path("list", VideoListView.as_view()),
    path("update", VideoUpdateView.as_view(), name="update"),
]
