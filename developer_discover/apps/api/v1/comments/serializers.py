from rest_framework import serializers

from apps.model.comments.models import Comment
from apps.model.users.models import User
from ..users.serializers import CurrentUserSerializer


class UserRelatedField(serializers.RelatedField):
    def to_representation(self, value):
        if isinstance(value, User):
            serializer = CurrentUserSerializer(value)
        else:
            raise Exception("Unexpected type of user object")
        return serializer.data


class CommentListSerializer(serializers.ModelSerializer):
    author = UserRelatedField(source="user", read_only=True)

    class Meta:
        model = Comment
        fields = ("id", "content", "author", "created_at", "updated_at")


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("content", "user", "post")


class CommentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
