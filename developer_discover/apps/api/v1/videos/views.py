from rest_framework.response import Response

from rest_framework.views import APIView
from .serializers import VideoSerializer
from ....model.videos.models import Video


class VideoListView(APIView):
    model = Video
    serializer = VideoSerializer

    def get(self, request):
        list = Video.objects.get(id=1)
        return Response(self.serializer.data)
