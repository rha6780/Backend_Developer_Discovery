from . import views
from django.urls import path, include


urlpatterns = [
    path("list", views.PostListView.as_view(), name="list"),
    path("", views.PostCreateView.as_view(), name="create"),
    path("<int:pk>", views.PostView.as_view(), name="post"),
    path("<int:post_id>/comments/", include("apps.api.v1.comments.urls")),
]
