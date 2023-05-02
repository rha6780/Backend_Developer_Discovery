from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

User = get_user_model()


class UserSignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("email", "name", "password")

    def save(self, request):
        user = super().save()
        user.email = self.validated_data["email"]
        user.name = self.validated_data["name"]
        user.set_password(self.validated_data["password"])
        user.save()
        return user

    def validate(self, data):
        email = data.get("email", None)
        password = data.get("password", None)
        validate_password(password)

        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError("user already exists")

        return data


class UserSignInSerializer(serializers.ModelSerializer, TokenObtainPairSerializer):
    class Meta:
        model = get_user_model()
        fields = ("email", "password")
