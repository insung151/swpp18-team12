from rest_framework import serializers

from accounts.models import User


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    username = serializers.CharField(read_only=True)
    password = serializers.CharField(
        min_length=8,
        write_only=True,
        required=True,
        style={'input_type': 'password'}
    )

    class Meta:
        model = User
        fields = ['email', 'username', 'password']
