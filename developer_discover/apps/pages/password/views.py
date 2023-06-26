from django_nextjs.render import render_nextjs_page_sync


def token(request, token):
    return render_nextjs_page_sync(request)


def email_check(request):
    return render_nextjs_page_sync(request)
