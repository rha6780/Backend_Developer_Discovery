from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSignUpSerializer(serializers.ModelSerializer):
    # def create(self, validated_data):
    #     user = User.objects.create_user(
    #         username=validated_data["username"],
    #         name=validated_data["name"],
    #         password=validated_data["password"],
    #     )
    #     return user

    class Meta:
        model = get_user_model()
        fields = ("username", "name", "password")

    def save(self, request):
        user = super().save()
        user.username = self.validated_data["username"]
        user.name = self.validated_data["name"]
        user.set_password(self.validated_data["password"])
        user.save()
        return user

    def validate(self, data):
        username = data.get("username", None)
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError("user already exists")
        return data


class UserSignInSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("username", "password")
