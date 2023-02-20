import requests
from django.conf import settings
from django.http import HttpResponseRedirect
from rest_framework.response import Response
from rest_framework.views import APIView

from django.shortcuts import redirect
from django.contrib.auth import login


class TokenView(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            return Response({"error_msg": "이미 로그인한 상태입니다."})
        client_id = settings.GITHUB_ID
        redirect_uri = "http://127.0.0.1:8000/accounts/login/github/callback"
        scope = "read:user"
        return redirect(
            f"https://github.com/login/oauth/authorize?client_id={client_id}&redirect_uri={redirect_uri}&scope={scope}"
        )
