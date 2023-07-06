from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication

from apps.api.utils.image import ImageSave
from apps.model.comments.models import Comment
from apps.model.posts.models import Post
from .serializers import CommentCreateSerializer, CommentUpdateSerializer, CommentListSerializer


class CommentListView(ListAPIView):
    model = Comment
    queryset = Comment.objects.all()
    serializer_class = CommentListSerializer
    authentication_classes = []
    permission_classes = []

    def get_queryset(self, **kwargs):
        return self.queryset.filter(post_id=self.kwargs["post_id"]).order_by("created_at")


class CommentCreateView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def post(self, request, **kwargs):
        request.data["user"] = request.user.id
        request.data["post"] = self.kwargs["post_id"]

        serializer = CommentCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response({"error_msg": serializer.error_messages}, status=status.HTTP_400_BAD_REQUEST)


class CommentView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def patch(self, request, **kwargs):
        pk = self.kwargs["pk"]
        comment = Comment.objects.get(id=pk)

        serializer = CommentUpdateSerializer(comment, data=request.data, partial=True)
        if comment.user.id == request.user.id:
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_200_OK)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_403_FORBIDDEN)

    def delete(self, request, **kwargs):
        pk = self.kwargs["pk"]
        comment = Comment.objects.get(id=pk)
        if comment is not None and comment.user.id == request.user.id:
            comment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_403_FORBIDDEN)


class CommentImageView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def patch(self, request):
        user = request.user
        if user is not None:
            image_name = ImageSave.save(self, request)

            return Response({"image": "/" + image_name}, status=status.HTTP_200_OK)
        return Response({"error_msg": "비 로그인 상태입니다."}, status=status.HTTP_401_UNAUTHORIZED)
