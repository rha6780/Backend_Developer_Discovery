from urllib import request
from django.contrib import admin
from django.urls import include
from django.urls import path

# from rest_framework_jwt.views import refresh_jwt_token
from . import views

urlpatterns = [
    path("", views.CommentListView.as_view(), name="comment-list"),
    path("", views.CommentCreateView.as_view(), name="comment-create"),
    path("/<int:pk>", views.CommentView.as_view(), name="comment"),
]
