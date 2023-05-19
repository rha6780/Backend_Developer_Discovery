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
            return Response({"id": user.id, "email": user.email, "name": user.name}, status.HTTP_200_OK)
        else:
            return Response({"error_msg": "비 로그인 상태입니다."}, status.HTTP_401_UNAUTHORIZED)


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
                return Response({"error_msg": "invalid email"}, status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error_msg": "비 로그인 상태입니다."}, status.HTTP_401_UNAUTHORIZED)


class ChangePasswordView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def patch(self, request):
        # TODO: 비밀번호 변경 로직 validation 관련 체크
        params = request.data
        user = request.user
        if user is not None:
            user.set_password(params["password"])
            user.save()
            return Response("{}", status.HTTP_200_OK)
        else:
            return Response("{}", status.HTTP_400_BAD_REQUEST)
