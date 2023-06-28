from rest_framework import serializers

from apps.model.posts.models import Post
from apps.model.users.models import User
from apps.model.comments.models import Comment
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
        fields = ("id", "title", "content", "thumbnail", "created_at", "updated_at", "author")


class PostUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("title", "content", "thumbnail")


class CommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("id", "content", "user", "created_at", "updated_at")
