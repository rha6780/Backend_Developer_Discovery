from django.contrib import admin
from django.http import request
from django.urls import path

from .views import AnswerListView
from .views import QuestionListView

urlpatterns = [
    path("question/<int:id>", QuestionListView.as_view(), name='question_item'),
    path("answer/<int:id>", AnswerListView.as_view()),
]
