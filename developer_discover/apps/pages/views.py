import requests

from django.shortcuts import render
import django.views as view
from django_nextjs.render import render_nextjs_page_sync


class HomeView(view.View):
    def get(self, request):
        return render_nextjs_page_sync(request)
