from rest_framework import serializers

from ....model.posts.models import Post
from ....model.users.models import User
from ..users.serializers import CurrentUserSerializer


class UserRelatedField(serializers.RelatedField):
    def to_representation(self, value):
        if isinstance(value, User):
            serializer = CurrentUserSerializer(value)
        else:
            raise Exception("Unexpected type of user object")
        return serializer.data


class PostListSerializer(serializers.ModelSerializer):
    author = UserRelatedField(source="user", read_only=True)

    class Meta:
        model = Post
        fields = ("id", "title", "content", "thumbnail", "author", "created_at")


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("title", "content", "thumbnail", "user")


class PostSerializer(serializers.ModelSerializer):
    author = UserRelatedField(source="user", read_only=True)

    class Meta:
        model = Post
        fields = ("id", "title", "content", "thumbnail", "created_at", "author")


class PostUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("title", "content", "thumbnail")
