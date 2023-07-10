from django_nextjs.render import render_nextjs_page_sync
from django_nextjs.render import render_nextjs_page


def index(request):
    return render_nextjs_page(request)


def signin(request):
    return render_nextjs_page(request)


def signup(request):
    return render_nextjs_page(request)


def profile(request):
    return render_nextjs_page(request)


def withdrawal(request):
    return render_nextjs_page(request)
