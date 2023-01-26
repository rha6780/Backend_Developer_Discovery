from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework.views import APIView

from .serializers import CurrentUserSerializer


class CurrentUserView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if request.user is not None:
            serializer = CurrentUserSerializer(request.user)
            return Response(serializer.data)
        else:
            return Response({"error_msg": "비 로그인 상태입니다."})
