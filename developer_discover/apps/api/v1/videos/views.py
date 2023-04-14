from django.core.paginator import Paginator

from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .serializers import VideoListSerializer, VideoUpdateInputSerializer
from ....model.videos.models import Video


class VideoListView(ListAPIView):
    model = Video
    queryset = Video.objects.all()
    serializer_class = VideoListSerializer
    permission_classes = []
    paginate_by = 10


class VideoUpdateView(APIView):
    model = Video
    serializer_class = VideoUpdateInputSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request):
        params = VideoUpdateInputSerializer(request.query_params)
        params.is_valid(raise_exception=True)
        Video.objects.create(title="title", introduction="", youtube_link="", user=self.request.user)
