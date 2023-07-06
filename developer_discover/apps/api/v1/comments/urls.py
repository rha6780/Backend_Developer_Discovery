from urllib import request
from django.contrib import admin
from django.urls import include
from django.urls import path

# from rest_framework_jwt.views import refresh_jwt_token
from . import views


app_name = "comments"
urlpatterns = [
    path("/list", views.CommentListView.as_view(), name="list"),
    path("", views.CommentCreateView.as_view(), name="create"),
    path("/image", views.CommentImageView.as_view(), name="image"),
    path("/<int:pk>", views.CommentView.as_view(), name="action"),
]
