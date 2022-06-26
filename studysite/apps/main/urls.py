from django.contrib import admin
from django.urls import path

from .views import MainView
from .views import QuestionViewSet

urlpatterns = [
    path("", MainView.as_view()),
    path("question", QuestionViewSet.as_view()),
]
