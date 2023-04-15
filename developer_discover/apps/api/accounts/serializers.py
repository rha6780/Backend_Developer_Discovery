from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSignUpSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        print("username 전달:", validated_data["username"])
        user = User.objects.create_user(
            username=validated_data["username"],
            name=validated_data["name"],
            password=validated_data["password"],
        )
        return user

    class Meta:
        model = get_user_model()
        fields = ("username", "name", "password")
