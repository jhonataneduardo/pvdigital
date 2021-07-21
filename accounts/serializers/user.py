from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from accounts.models.user import User


class ListCreateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'first_name', 'password']
        extra_kwargs = {
            'password': {'write_only': True},
            'first_name': {'write_only': True, 'required': True}
        }

    def create(self, validated_data):
        username = None
        if validated_data.get('username', False):
            username = validated_data['username']
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            username=username,
        )
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email']
