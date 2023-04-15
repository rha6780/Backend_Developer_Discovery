from email import header
import requests
from django.conf import settings
from django.http import HttpResponseRedirect

from django.shortcuts import redirect
from django.contrib.auth import login

from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


# from ...model.users.models import User
from .serializers import UserSignUpSerializer

User = get_user_model()


class UserSignUpView(CreateAPIView):
    model = User
    queryset = User.objects.all()
    authentication_classes = []
    permission_classes = []
    serializer_class = UserSignUpSerializer

    # def post(self, request, *args, **kwargs):
    #     payload = request.data

    #     serializer = self.get_serializer(data=payload)
    #     # serializer.create()
    #     user = User.objects.get(email=payload["email"])
    #     print(payload["email"], user)
    #     login(request, user)
    #     return HttpResponseRedirect("http://localhost:8000")


class GithubSocialLoginView(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        if request.user.is_authenticated:
            return Response({"error_msg": "이미 로그인한 상태입니다."})
        client_id = settings.GITHUB_ID
        redirect_uri = "http://127.0.0.1:8000/accounts/login/github/callback"
        scope = "read:user"
        return redirect(
            f"https://github.com/login/oauth/authorize?client_id={client_id}&redirect_uri={redirect_uri}&scope={scope}"
        )


class GithubCallBackView(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        if request.user.is_authenticated:
            return Response({"error_msg": "이미 로그인한 상태입니다."})
        code = request.GET.get("code", None)
        if code is None:
            return Response({"error_msg": "code 값이 없습니다."})

        client_id = settings.GITHUB_ID
        client_secret = settings.GITHUB_SECRET

        github_request = requests.post(
            f"https://github.com/login/oauth/access_token?client_id={client_id}&client_secret={client_secret}&code={code}",
            headers={"Accept": "application/json"},
        )
        token_json = github_request.json()
        error = token_json.get("error", None)
        if error is not None:
            return Response({"error_msg": f"{error}"})
        access_token = token_json.get("access_token")
        profile_request = requests.get(
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
                name=name,
                email=email,
            )

            user.set_unusable_password()
            user.save()

        login(request, user)
        if user is not None:
            if user.is_active:
                refresh = RefreshToken.for_user(user)
                return Response(
                    {
                        "refresh": str(refresh),
                        "access": str(refresh.access_token),
                    },
                    status=status.HTTP_200_OK,
                )
        return HttpResponseRedirect("http://localhost:3000")
