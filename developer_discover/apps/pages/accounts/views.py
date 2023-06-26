from django_nextjs.render import render_nextjs_page_sync


def password_change(request):
    return render_nextjs_page_sync(request)


def email_change(request):
    return render_nextjs_page_sync(request)
