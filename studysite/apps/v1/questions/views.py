from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Question
from .serializers import QuestionSerializer

class QuestionListView(APIView):
    model = Question
    serializer_class = QuestionSerializer

    def get(self, request):
        queryset = self.model.objects.all
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

class QuestionItemView(APIView):
    model = Question
    serializer_class = QuestionSerializer

    def get(self, request, id):
        queryset = self.model.objects.filter(id=id)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
