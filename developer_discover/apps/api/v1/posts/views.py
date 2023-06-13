from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated, AllowAny
from ....model.posts.models import Post


from .serializers import PostListSerializer, PostCreateSerializer, PostSerializer


# TODO: 추후 삭제할 것
class PostListView(ListAPIView):
    model = Post
    queryset = Post.objects.all().order_by("-created_at")
    serializer_class = PostListSerializer
    permission_classes = []


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all().order_by("-created_at")
    serializer_class = PostSerializer
    # pagination_class = StudentPagination # 👈 pagination_class 값에 매핑
    permission_classes_by_action = {"create": [IsAuthenticated], "list": [AllowAny]}

    def create(self, request, *args, **kwargs):
        return super(PostViewSet, self).create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        return super(PostViewSet, self).list(request, *args, **kwargs)

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]

    def get_serializer_class(self):
        if self.action == "list":
            return PostListSerializer

        return super().get_serializer_class()
