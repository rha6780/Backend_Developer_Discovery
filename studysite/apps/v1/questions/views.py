from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Question
from .serializers import QuestionCategoryListSerializer
from .serializers import QuestionItemSerializer


class QuestionItemView(APIView):
    model = Question
    serializer_class = QuestionItemSerializer

    def get(self, request, id):
        queryset = self.model.objects.filter(id=id)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class QuestionCategoryListView(APIView):
    model = Question
    serializer_class = QuestionCategoryListSerializer

    def get(self, request, category):
        queryset = self.model.objects.filter(category=category)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
