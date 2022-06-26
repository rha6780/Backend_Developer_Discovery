from django.contrib import admin
from django.urls import path

from .views import MainView
from .views import QuestionView

urlpatterns = [
    path("", MainView.as_view()),
    path("question/", QuestionView.as_view()),
]
