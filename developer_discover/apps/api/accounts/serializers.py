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
        fields = ("email", "name", "password")

    def save(self, request):
        user = super().save()
        user.email = self.validated_data["email"]
        user.name = self.validated_data["name"]
        user.set_password(self.validated_data["password"])
        user.save()
        return user

    # def validate_password(self, password):
    #     if password:
    #         raise serializers.ValidationError("password invalid")

    def validate(self, data):
        email = data.get("email", None)
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError("user already exists")
        return data


class UserSignInSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("email", "password")
