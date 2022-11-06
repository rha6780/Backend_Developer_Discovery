from django.contrib import admin
from django.urls import include
from django.urls import path


urlpatterns = [
    path("answers/", include("apps.v1.answers.urls")),
    path("questions/", include("apps.v1.questions.urls")),
    path("scores/", include("apps.v1.scores.urls")),
]
