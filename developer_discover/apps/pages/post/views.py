from django_nextjs.render import render_nextjs_page_sync


def detail(request, id):
    return render_nextjs_page_sync(request)


def edit(request, id):
    return render_nextjs_page_sync(request)


def new(request):
    return render_nextjs_page_sync(request)
