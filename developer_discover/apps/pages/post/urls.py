from django.contrib import admin
from django.urls import include
from django.urls import path
from . import views

urlpatterns = [
    path("<int:id>", views.detail, name="detail"),
    path("edit/<int:id>", views.edit, name="edit"),
    path("new", views.new, name="new"),
]
