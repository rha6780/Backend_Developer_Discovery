from django.contrib import admin
from django.http import request
from django.urls import path

from .views import QuestionItemView

urlpatterns = [
    path("<int:id>", QuestionItemView.as_view(), name="question_item"),
]
