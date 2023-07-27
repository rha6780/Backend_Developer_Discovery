from . import views
from django.urls import path, include


app_name = "posts"
urlpatterns = [
    path("/list", views.PostListView.as_view(), name="list"),
    path("", views.PostCreateView.as_view(), name="create"),
    path("/image", views.PostImageView.as_view(), name="image"),
    path("/<int:pk>", views.PostView.as_view(), name="action"),
    path("/like/<int:pk>", views.PostLikeView.as_view(), name="like"),
    path("/<int:post_id>/comments", include("apps.api.v1.comments.urls", namespace="comments")),
]
