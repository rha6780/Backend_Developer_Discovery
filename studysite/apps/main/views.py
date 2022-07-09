from rest_framework.response import Response
from rest_framework.views import APIView

from django import views
from django.shortcuts import render

from .models import Answer
from .models import Question
from .serializers import AnswerSerializer
from .serializers import QuestionSerializer


class MainView(views.View):
    def get(self, request):
        return render(request, "main/index.html")


class QuestionListView(APIView):
    serializer_class = QuestionSerializer

    def get(self, request):
        queryset = Question.objects.all()
        serializer = self.serializer_class(queryset)
        return Response(serializer.data)


class AnswerListView(APIView):
    serializer_class = AnswerSerializer

    def get(self, request):
        queryset = Answer.objects.all()
        serializer = self.serializer_class(queryset)
        return Response(serializer.data)
