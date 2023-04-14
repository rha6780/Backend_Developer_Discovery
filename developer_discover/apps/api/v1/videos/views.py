from rest_framework import status
from rest_framework.response import Response
from django.core.paginator import Paginator

from rest_framework.views import APIView
from .serializers import VideoSerializer
from ....model.videos.models import Video


class VideoListView(APIView):
    model = Video
    serializer_class = VideoSerializer
    permission_classes = []

    def get(self, request):

        # TODO: 모델에 카테고리를 넣고 해당 카테고리에 해당하는 값을 반환 하도록 수정
        data = Video.objects.first

        if data == None:
            return Response("data")

        serializer = VideoSerializer(data)
        return Response(
            {
                "videos": serializer.data,
            },
            status=status.HTTP_200_OK,
        )
