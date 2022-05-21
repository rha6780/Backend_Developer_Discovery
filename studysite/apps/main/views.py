from django import views
from django.shortcuts import render


# Create your views here.
class MainView(views.View):
    def main(request):
        render(request, "templates/main.html")
