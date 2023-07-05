import uuid
import os

from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password

from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework import status
from rest_framework.views import APIView

from drf_yasg.utils import swagger_auto_schema

from django.conf import settings
from .serializers import UserImageSerializer


class UserView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        if request.user is not None:
            return Response(
                {"id": user.id, "email": user.email, "name": user.name, "image": user.profile_image.url},
                status=status.HTTP_200_OK,
            )
        else:
            return Response({"error_msg": "비 로그인 상태입니다."}, status=status.HTTP_401_UNAUTHORIZED)

    def patch(self, request):
        user = request.user
        email = request.data["changed_email"]
        name = request.data["changed_name"]
        if request.user is not None:
            if name in [None, "", " "] and email in [None, "", " "]:
                return Response({"error_msg": "invalid email"}, status=status.HTTP_400_BAD_REQUEST)
            else:
                if email not in [None, "", " "]:
                    user.email = email
                if name not in [None, "", " "]:
                    user.name = name
                user.save()
                return Response({"id": user.id, "email": user.email, "name": user.name}, status.HTTP_200_OK)
        else:
            return Response({"error_msg": "비 로그인 상태입니다."}, status=status.HTTP_401_UNAUTHORIZED)


class ChangePasswordView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        tags=["유저 계정 관련 API"], manual_parameters=[], responses={200: "Success", 400: "유효하지 않은 비밀번호", 401: "인증되지 않은 사용자"}
    )
    def patch(self, request):
        params = request.data
        user = request.user
        if user is not None:
            try:
                validate_password(params["changed_password"], user=user)
                user.set_password(params["changed_password"])
                user.save()
                return Response({"msg": "success!"}, status=status.HTTP_200_OK)
            except ValidationError:
                return Response({"error_msg": "비밀번호가 올바르지 않습니다."}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error_msg": "유저정보가 올바르지 않습니다."}, status=status.HTTP_401_UNAUTHORIZED)
