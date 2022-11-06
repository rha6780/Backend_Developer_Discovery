from rest_framework import serializers

from .models import Question


class QuestionItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"


class QuestionCategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"
