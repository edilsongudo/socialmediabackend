from rest_framework import serializers
from django.contrib.auth.models import User
from core.serializers import PostSerializer


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    post_set = PostSerializer(read_only=True, many=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'post_set')


# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password'])

        return user
