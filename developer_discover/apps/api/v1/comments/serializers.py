from rest_framework import serializers

from apps.model.comments.models import Comment


class CommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("id", "content", "user", "created_at", "updated_at")


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("content", "user", "post")


class CommentUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
