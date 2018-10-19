import re

from rest_framework import serializers

from accounts.fields import PasswordField
from accounts.models import User, UserProfile


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    username = serializers.CharField(read_only=True)
    password = PasswordField()

    class Meta:
        model = User
        fields = ['email', 'username', 'password']


class SignUpSerializer(serializers.Serializer):
    email = serializers.EmailField()
    username = serializers.CharField()
    password = PasswordField()
    password_confirmation = PasswordField()
    year_of_admission = serializers.IntegerField(
        max_value=2500,
        min_value=1800,
        required=False
    )
    department = serializers.CharField(max_length=20, required=False)

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError('Already exists')
        return value

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError('Already exists')
        return value

    def validate_password(self, value):
        pattern = r'^(?=.*\d)(?=.*[a-zA-Z])'
        if not re.match(pattern, value):
            raise serializers.ValidationError("Invalid password")
        return value

    def validate_password_confirmation(self, value):
        password = self.get_initial().get('password')
        if password != value:
            raise serializers.ValidationError("Password must be same")
        return value

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password']
        )
        UserProfile.objects.create(
            user=user,
            year_of_admission=validated_data.get('year_of_admission', None),
            department=validated_data.get('department', None)
        )
        return user


class ChangePasswordSerializer(serializers.Serializer):
    old_password = PasswordField()
    new_password = PasswordField()

    def validate_new_password(self, value):
        if (value == self.initial_data['old_password']):
            raise serializers.ValidationError("New password must be different with old")
        return value
