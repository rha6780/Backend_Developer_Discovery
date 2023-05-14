from django.core.paginator import Paginator

from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import Permission

from .serializers import VideoListSerializer, VideoUpdateInputSerializer
from .paginations import VideoListPagination
from ....model.videos.models import Video


class VideoListView(ListAPIView):
    model = Video
    queryset = Video.objects.all()
    serializer_class = VideoListSerializer
    permission_classes = []
    pagination_class = VideoListPagination
    page_size = 4


class VideoCreateView(CreateAPIView):
    model = Video
    serializer_class = VideoUpdateInputSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        payload = request.data
        payload["user"] = request.user

        # serializer = self.get_serializer(data=payload)
