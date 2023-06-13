from rest_framework import serializers

from ....model.posts.models import Post


class PostListSerializer(serializers.ModelSerializer):
    user_name = serializers.RelatedField(source="users.User.name", read_only=True)

    class Meta:
        model = Post
        fields = ("id", "title", "content", "thumbnail", "user_name")
