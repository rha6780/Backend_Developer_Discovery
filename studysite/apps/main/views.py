from tkinter.messagebox import QUESTION
from django import views
from django.shortcuts import render
from .models import Question
from rest_framework.views import APIView


# Create your views here.
class MainView(views.View):
    def get(self, request):
        return render(request, "main/index.html")

class QuestionList(APIView):
    def get(self, request):
        question = Question.objects.all()
        return question