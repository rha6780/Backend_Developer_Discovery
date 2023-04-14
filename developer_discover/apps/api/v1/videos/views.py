from rest_framework import status
from rest_framework.response import Response
from django.core.paginator import Paginator

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import VideoListSerializer, VideoUpdateInputSerializer
from ....model.videos.models import Video


class VideoListView(APIView):
    model = Video
    serializer_class = VideoListSerializer
    permission_classes = []

    def get(self, request):
        # TODO: 모델에 카테고리를 넣고 해당 카테고리에 해당하는 값을 반환 하도록 수정
        try:
            data = Video.objects.first
        except Video.DoesNotExist:
            return Response("data")

        if data == None:
            return Response("data")

        serializer = VideoListSerializer(data)
        return Response(
            {
                "videos": "data",
            },
            status=status.HTTP_200_OK,
        )


class VideoUpdateView(APIView):
    model = Video
    serializer_class = VideoUpdateInputSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request):
        params = VideoUpdateInputSerializer(request.query_params)
        params.is_valid(raise_exception=True)
        Video.objects.create(title="title", introduction="", youtube_link="", user=self.request.user)
