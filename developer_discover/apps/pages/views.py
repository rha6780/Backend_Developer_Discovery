from django.shortcuts import render
import django.views as view


from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "./html/index.html"
