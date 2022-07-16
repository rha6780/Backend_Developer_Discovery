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

    def get(self, request):
        queryset = self.model.objects.all()
        print(queryset)
        serializer = self.serializer_class(queryset, many=True)
        print(serializer.data)
        return Response(serializer.data)


class AnswerListView(APIView):
    model = Answer
    serializer_class = AnswerSerializer

    def get(self, request):
        queryset = self.model.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
