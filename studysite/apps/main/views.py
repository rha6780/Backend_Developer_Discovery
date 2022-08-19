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
