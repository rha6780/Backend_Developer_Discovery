from ....model.videos.models import Video
from rest_framework import serializers


class VideoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = (
            "id",
            "title",
            "user",
        )


class VideoUpdateInputSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=512, default="")
    introduction = serializers.CharField(max_length=1024, default="")
    youtube_link = serializers.CharField(max_length=2048, default="")
