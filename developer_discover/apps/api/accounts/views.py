from django.conf import settings
import environ

from django import views
from django.shortcuts import redirect


class GithubSocialLoginView(views.View):
    def get(self, request):
        if request.user.is_authenticated:
            raise Exception("User already logged in")
        client_id = settings.GITHUB_ID
        redirect_uri = "http://127.0.0.1:8000/accounts/login/github/callback/"
        scope = "read:user"
        return redirect(
            f"https://github.com/login/oauth/authorize?client_id={client_id}&redirect_uri={redirect_uri}&scope={scope}"
        )

    def callback(self, request):
        if request.user.is_authenticated:
            raise Exception("already logged in")
        code = request.GET.get("code", None)
        if code is None:
            raise Exception("code not found")

        client_id = settings.GITHUB_ID
        client_secret = settings.GITHUB_SECRET

        github_request = request.post(
            f"https://github.com/login/oauth/access_token?client_id={client_id}&client_secret={client_secret}&code={code}",
            headers={"Accept": "application/json"},
        )
        token_json = github_request.json()
        error = token_json.get("error", None)
