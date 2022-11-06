from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Answer
from ..serializers import AnswerSerializer


class AnswerListView(APIView):
    model = Answer
    serializer_class = AnswerSerializer

    def get(self, request, id):
        queryset = queryset = self.model.objects.filter(question_id=id)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
