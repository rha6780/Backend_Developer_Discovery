from django.contrib import admin
from django.http import request
from django.urls import path

from .views import AnswerListView
from .views import MainView
from .views import QuestionListView

urlpatterns = [
    path("", MainView.as_view()),
    path("question/", QuestionListView.as_view()),
    path("answer/", AnswerListView.as_view()),
]
