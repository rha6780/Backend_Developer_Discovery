from django.conf import settings
from django.http import HttpResponseRedirect
from rest_framework.response import Response
from rest_framework.views import APIView

from django.shortcuts import redirect
from django.contrib.auth import login

from ...model.users.models import User


class GithubSocialLoginView(APIView):
    # TODO: 로그인 시 page_not_found 에러 해결하기
    def get(self, request):
        if request.user.is_authenticated:
            return Response({"error_msg": "이미 로그인한 상태입니다."})
        client_id = settings.GITHUB_ID
        redirect_uri = "http://127.0.0.1:8000/accounts/login/github/callback/"
        scope = "read:user"
        return redirect(
            f"https://github.com/login/oauth/authorize?client_id={client_id}&redirect_uri={redirect_uri}&scope={scope}"
        )

    def callback(self, request):
        if request.user.is_authenticated:
            return Response({"error_msg": "이미 로그인한 상태입니다."})
        code = request.GET.get("code", None)
        if code is None:
            return Response({"error_msg": "code 값이 없습니다."})

        client_id = settings.GITHUB_ID
        client_secret = settings.GITHUB_SECRET

        github_request = request.post(
            f"https://github.com/login/oauth/access_token?client_id={client_id}&client_secret={client_secret}&code={code}",
            headers={"Accept": "application/json"},
        )
        token_json = github_request.json()
        error = token_json.get("error", None)
        if error is not None:
            return Response({"error_msg": f"{error}"})
        access_token = token_json.get("access_token")
        profile_request = request.get(
            "https://api.github.com/user",
            headers={
                "Authorization": f"token {access_token}",
                "Accept": "application/json",
            },
        )
        profile_response = profile_request.json()
        username = profile_response.get("login", None)
        email = profile_response.get("email", None)
        name = profile_response.get("name", None)
        if username is None:
            return Response({"error_msg": "Request에 username이 없습니다."})
        elif name is None:
            return Response({"error_msg": "Request에 name이 없습니다."})
        elif email is None:
            return Response({"error_msg": "Request에 email이 없습니다."})

        try:
            user = User.objects.get(email=email)

        except User.DoesNotExist:
            user = User.objects.create(
                username=email,
                first_name=name,
                email=email,
                login_method=User.LOGIN_GITHUB,
            )

            user.set_unusable_password()
            user.save()
        login(request, user)
        return HttpResponseRedirect(redirect_to="http://127.0.0.1:3000")
