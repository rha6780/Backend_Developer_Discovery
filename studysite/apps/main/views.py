from rest_framework.response import Response
from rest_framework.views import APIView

from django import views
from django.shortcuts import render

from .models import Answer, Score
from .models import Question
from .serializers import AnswerSerializer
from .serializers import ScoreSerializer
from .serializers import QuestionSerializer

class QuestionListView(APIView):
    model = Question
    serializer_class = QuestionSerializer

    def get(self, request, id):
        queryset = self.model.objects.filter(id=id)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class AnswerListView(APIView):
    model = Answer
    serializer_class = AnswerSerializer

    def get(self, request, id):
        queryset = queryset = self.model.objects.filter(question_id=id)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

class ScoreView(APIView):
    model = Score
    serializer_class = ScoreSerializer

    def get(self, request, name):
        queryset = queryset = self.model.objects.filter(name = name)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
