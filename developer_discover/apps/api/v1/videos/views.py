from rest_framework.response import Response

from rest_framework.views import APIView
from ....model.videos.models import Video


class VideoListView(APIView):
    model = Video

    def get(self, request):
        list = Video.objects.get(id=1)
