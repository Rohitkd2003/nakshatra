from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User
from rest_framework_simplejwt.tokens import RefreshToken


# -------------------------------
# USER DETAIL SERIALIZER
# -------------------------------
class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "full_name", "phone", "role"]


# -------------------------------
# USER SERIALIZER (BASIC)
# -------------------------------
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "full_name", "phone", "role"]


# -------------------------------
# REGISTER SERIALIZER
# -------------------------------
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "password", "full_name", "phone", "role"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data["email"],
            password=validated_data["password"],
            full_name=validated_data["full_name"],
            phone=validated_data["phone"],
            role=validated_data["role"],
        )
        return user


# -------------------------------
# LOGIN SERIALIZER
# -------------------------------
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(email=data["email"], password=data["password"])

        if not user:
            raise serializers.ValidationError("Invalid credentials")

        # Generate tokens
        refresh = RefreshToken.for_user(user)

        # Return full user details + tokens
        return {
            "access": str(refresh.access_token),
            "refresh": str(refresh),
            "user": UserDetailSerializer(user).data,
        }
