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
            print(user.email)
            return Response({"id": user.id, "email": user.email, "name": user.name}, status.HTTP_200_OK)
        else:
            return Response({"error_msg": "비 로그인 상태입니다."})
