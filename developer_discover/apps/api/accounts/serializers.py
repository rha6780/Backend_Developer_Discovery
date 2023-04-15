from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSignUpSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data["email"],
            name=validated_data["name"],
            password=validated_data["password"],
        )
        return user

    class Meta:
        model = get_user_model()
        fields = ("email", "name", "password")
