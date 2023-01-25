from rest_framework.response import Response
from rest_framework import status

from rest_framework.views import APIView

from ....model.users.models import User
from .serializers import UserSerializer


class UserView(APIView):
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
