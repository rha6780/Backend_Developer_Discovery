from django.contrib import admin
from django.urls import include
from django.urls import path

from .views import VideoListView, VideoCreateView


urlpatterns = [
    path("list", VideoListView.as_view(), name="list"),
    path("create", VideoCreateView.as_view(), name="create"),
]
