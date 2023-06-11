from ....model.videos.models import Video
from rest_framework import serializers


class VideoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = (
            "id",
            "title",
            "introduction",
            "user",
            "youtube_link",
            "thumbnail",
        )


class VideoCreateSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=512, default="")
    introduction = serializers.CharField(max_length=512, default="")
    youtube_link = serializers.CharField(max_length=1024, default="")

    class Meta:
        model = Video
        fields = ("title", "introduction", "youtube_link")
