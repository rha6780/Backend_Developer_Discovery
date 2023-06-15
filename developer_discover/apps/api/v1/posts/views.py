from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from ....model.posts.models import Post


from .serializers import PostListSerializer, PostCreateSerializer, PostSerializer, PostUpdateSerializer


class PostListView(generics.ListAPIView):
    model = Post
    queryset = Post.objects.all().order_by("-created_at")
    serializer_class = PostListSerializer
    permission_classes = []


class PostCreateView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = PostCreateSerializer

    def post(self, request, *args, **kwargs):
        request.data["user"] = request.user.id

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        print(serializer.errors)
        return Response(data=serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)


class PostView(APIView):
    # authentication_classes = [JWTAuthentication]
    permission_classes = []

    def get(self, request, *args, **kwargs):
        pk = self.kwargs["pk"]
        post = Post.objects.get(id=pk)
        if post is not None:
            serializer = PostSerializer(post)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data={"msg": "not_found"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        self.authentication_classes = JWTAuthentication
        self.permission_classes = IsAuthenticated
        pk = self.kwargs["pk"]
        post = Post.objects.get(id=pk)
        if post.user.id == request.user.id:
            post.soft_delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_403_FORBIDDEN)

    def patch(self, request, *args, **kwargs):
        self.authentication_classes = JWTAuthentication
        self.permission_classes = IsAuthenticated
        pk = self.kwargs["pk"]
        post = Post.objects.get(id=pk)
        serializer = PostUpdateSerializer(data=request.data)
        if post.user.id == request.user.id:
            if serializer.is_valid():
                serializer.save()
                return Response(status.HTTP_200_OK)
            return Response(status.HTTP_400_BAD_REQUEST)
        return Response(status.HTTP_403_FORBIDDEN)
