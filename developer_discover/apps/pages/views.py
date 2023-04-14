import requests

from django.shortcuts import render
import django.views as view


from django.views.generic import TemplateView


class HomeView(view.View):
    def get(self, request):
        res = requests.get("https://localhost:3000")
        return render(res)
