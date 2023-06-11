from django.core.paginator import Paginator

from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth.models import Permission

from .serializers import VideoListSerializer, VideoCreateSerializer
from .paginations import VideoListPagination
from ....model.videos.models import Video


class VideoListView(ListAPIView):
    model = Video
    queryset = Video.objects.all()
    serializer_class = VideoListSerializer
    permission_classes = []
    pagination_class = VideoListPagination
    page_size = 4


class VideoCreateView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = VideoCreateSerializer

    def post(self, request):
        payload = request.data
        payload["user"] = request.user
        print(request.user)

        serializer = self.serializer_class(data=payload)
        if serializer.is_valid():
            Video.objects.create(serializer)
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
