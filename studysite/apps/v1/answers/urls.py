from django.contrib import admin
from django.http import request
from django.urls import path

from .views import AnswerListView, AnswerCategoryListView

urlpatterns = [
    path("<int:id>", AnswerListView.as_view()),
    path("<str:category>", AnswerCategoryListView.as_view()),
]
