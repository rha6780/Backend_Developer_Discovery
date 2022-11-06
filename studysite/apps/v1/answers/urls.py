from django.contrib import admin
from django.http import request
from django.urls import path

from .views import AnswerListView

urlpatterns = [
    path("<int:id>", AnswerListView.as_view()),
]
