from email import header
import requests
from django.conf import settings
from django.http import HttpResponseRedirect

from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth.hashers import check_password
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

from rest_framework.authtoken.models import Token

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# Email
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes

# from .tokens import account_activation_token

# from ...model.users.models import User
from .serializers import UserSignUpSerializer, UserSignInSerializer, UserPasswordResetSerializer

User = get_user_model()


class UserSignUpView(APIView):
    model = User
    queryset = User.objects.all()
    authentication_classes = []
    permission_classes = []
    serializer_class = UserSignUpSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            user = serializer.save(request=request)
            token = TokenObtainPairSerializer.get_token(user)
            refresh_token = str(token)
            access_token = str(token.access_token)
            res = Response(
                {
                    "user": request.data["email"],
                    "message": "user register successs",
                    "token": {
                        "access": access_token,
                        "refresh": refresh_token,
                    },
                },
                status=status.HTTP_200_OK,
            )
            res.set_cookie("access", access_token, httponly=True, secure=True)
            res.set_cookie("refresh", refresh_token, httponly=True, secure=True)
            return res
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserSignInView(APIView):
    model = User
    authentication_classes = []
    permission_classes = []
    serializer_class = UserSignInSerializer

    def post(self, request):
        params = request.data
        user = User.objects.filter(email=params["email"]).first()

        if user is not None:
            if not check_password(params["password"], user.password):
                return Response({"message": "password invalid"}, status=status.HTTP_400_BAD_REQUEST)
            token = TokenObtainPairSerializer.get_token(user)
            refresh_token = str(token)
            access_token = str(token.access_token)
            res = Response(
                {
                    "user": params["email"],
                    "message": "login success",
                    "token": {
                        "access": access_token,
                        "refresh": refresh_token,
                    },
                },
                status=status.HTTP_200_OK,
            )
            res.set_cookie("access", access_token, httponly=True, secure=True)
            res.set_cookie("refresh", refresh_token, httponly=True, secure=True)
            return res
        return Response({"message": "user not found"}, status=status.HTTP_400_BAD_REQUEST)


class UserEmailConfirmView(APIView):
    model = User
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        email = request.data.get("email")
        user = User.objects.get(email=email)
        token, is_created = Token.objects.get_or_create(user=user)
        current_site = get_current_site(request)
        message = render_to_string(
            "reset_password.html",
            {
                "domain": current_site.domain,
                "uid": urlsafe_base64_encode(force_bytes(email)),
                "token": str(token),
            },
        )
        mail_title = "Developer Discovery - 비밀번호 재설정 메일"
        email = EmailMessage(mail_title, message, to=[email])
        email.content_subtype = "html"
        email.send()
        return Response({"message": "Email Sending"}, status=status.HTTP_200_OK)


class UserPasswordResetView(APIView):
    model = User
    permission_classes = []
    serializer_class = UserPasswordResetSerializer

    def post(self, request, *args, **kwags):
        params = request.data
        serializer = self.serializer_class(data=params)
        token = Token.objects.get(key=params["token"])

        if token is None:
            return Response({"message": "Invalid token"}, status.HTTP_404_NOT_FOUND)
        if not serializer.is_valid():
            print(params["password"], serializer.is_valid())
            return Response({"message": "Invalid password"}, status.HTTP_400_BAD_REQUEST)
        user = User.objects.get(id=token.user_id)
        user.set_password(params["password"])
        user.save()
        token.delete()
        return Response({"message": "Update compelete"}, status.HTTP_200_OK)


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
