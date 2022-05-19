from django.contrib import admin
from django.urls import include
from django.urls import path

from .views import MainView

urlpatterns = [
    path('', MainView.as_view()),
]
