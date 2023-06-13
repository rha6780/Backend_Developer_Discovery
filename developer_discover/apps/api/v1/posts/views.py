from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import ListAPIView, CreateAPIView
from ....model.posts.models import Post

from .serializers import PostListSerializer


class PostListView(ListAPIView):
    model = Post
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    permission_classes = []


class VideoCreateView(CreateAPIView):
    """TODO: 로직 작성"""
