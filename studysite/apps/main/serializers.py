from rest_framework import serializers

from .models import Question


class QuestionSerializer(serializers.Serializer):
    category = serializers.CharField(max_length=50)
    content = serializers.CharField(max_length=1_000)
    Answer_count = serializers.IntegerField(default=2)
