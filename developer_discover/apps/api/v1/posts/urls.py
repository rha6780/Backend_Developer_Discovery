from . import views
from django.contrib import admin
from django.urls import include
from django.urls import path

from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r"", views.PostViewSet, basename="posts")

urlpatterns = [
    path("list", views.PostListView.as_view(), name="list"),
    path("create", views.PostCreateView.as_view(), name="create"),
    path("<int:pk>", views.PostView.as_view(), name="post"),
]
