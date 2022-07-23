from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['email', 'token']

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)
