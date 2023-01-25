from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    class Meta:
        model = get_user_model
        fields = ("id", "email", "name")
