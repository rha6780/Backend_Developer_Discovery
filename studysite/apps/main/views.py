from rest_framework.views import ListAPIView

from django import views
from django.shortcuts import render

from .models import Question
from .serializers import QuestionSerializer


# Create your views here.
class MainView(views.View):
    def get(self, request):
        return render(request, "main/index.html")


class QuestionList(ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
