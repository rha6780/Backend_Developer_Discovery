from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password

from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework import status
from rest_framework.views import APIView

# from .serializers import CurrentUserSerializer


class CurrentUserView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        if request.user is not None:
            return Response({"id": user.id, "email": user.email, "name": user.name}, status=status.HTTP_200_OK)
        else:
            return Response({"error_msg": "비 로그인 상태입니다."}, status=status.HTTP_401_UNAUTHORIZED)


class ChangeEmailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def patch(self, request):
        user = request.user
        email = request.data["changed_email"]
        if request.user is not None:
            if email not in [None, "", " "]:
                user.email = email
                user.save()
                return Response({"id": user.id, "email": user.email, "name": user.name}, status.HTTP_200_OK)
            else:
                return Response({"error_msg": "invalid email"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error_msg": "비 로그인 상태입니다."}, status=status.HTTP_401_UNAUTHORIZED)


class ChangePasswordView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

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
