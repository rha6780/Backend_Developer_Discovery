from . import views
from django.urls import path


urlpatterns = [
    path("list", views.PostListView.as_view(), name="list"),
    path("", views.PostCreateView.as_view(), name="create"),
    path("<int:pk>", views.PostView.as_view(), name="post"),
    path("<int:pk>/comments", views.CommentListView.as_view(), name="comment-list"),
]
