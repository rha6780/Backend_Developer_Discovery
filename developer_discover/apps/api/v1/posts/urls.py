from . import views
from django.contrib import admin
from django.urls import include
from django.urls import path

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"", views.PostViewSet, basename="posts")

urlpatterns = [
    # path("list", views.PostListView.as_view(), name="list"),
    path("", include(router.urls)),
]
