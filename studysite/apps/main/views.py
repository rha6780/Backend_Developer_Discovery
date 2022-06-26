from rest_framework.views import APIView

from django import views
from django.shortcuts import render

from .models import Question
from .serializers import QuestionSerializer


# Create your views here.
class MainView(views.View):
    def get(self, request):
        return render(request, "main/index.html")


class QuestionViewSet(APIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
