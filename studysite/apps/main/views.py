from django import views
from django.shortcuts import render


# Create your views here.
class MainView(views.View):
    def get(self, request):
        return render(request, "main/index.html")
