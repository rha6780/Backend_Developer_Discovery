from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Score
from .serializers import ScoreSerializer

class ScoreView(APIView):
    model = Score
    serializer_class = ScoreSerializer

    def get(self, request, name):
        queryset = queryset = self.model.objects.filter(name = name)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
