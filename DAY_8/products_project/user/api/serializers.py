from rest_framework import serializers
from django.contrib.auth.models import User
from ..models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class PasswordSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=20)
    