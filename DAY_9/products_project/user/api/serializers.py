from rest_framework import serializers
from django.contrib.auth.models import User
from ..models import Profile
from django.contrib.auth.hashers import make_password, check_password

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"



class PasswordSerializer(serializers.Serializer):
    new_password = serializers.CharField(write_only=True, max_length=20)
    old_password = serializers.CharField(write_only=True, max_length=20, required=False)

    def validate_old_password(self, value):
        user = self.context['request'].user

        if not check_password(value, user.password):
            raise serializers.ValidationError("Eski şifre yanlış.")
        
        return value

    def create(self, validated_data):
        new_password = validated_data['new_password']
        return make_password(new_password)


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        # fields = "__all__"
        exclude = ["last_login", "date_joined", "groups", "user_permissions"]

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        user = User.objects.create(**validated_data)
        return user
    
    