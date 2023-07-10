from django_nextjs.render import render_nextjs_page_sync
from django_nextjs.render import render_nextjs_page


async def index(request):
    return await render_nextjs_page(request)


async def signin(request):
    return await render_nextjs_page(request)


async def signup(request):
    return await render_nextjs_page(request)


async def profile(request):
    return await render_nextjs_page(request)


async def withdrawal(request):
    return await render_nextjs_page(request)
