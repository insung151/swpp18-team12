import re

from rest_framework import serializers

from accounts.models import User, UserProfile


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


class SignUpSerializer(serializers.Serializer):
    email = serializers.EmailField()
    username = serializers.CharField()
    password = serializers.CharField(
        min_length=8,
        write_only=True,
        required=True,
        style={'input_type': 'password'}
    )
    password_confirmation = serializers.CharField(
        min_length=8,
        write_only=True,
        required=True,
        style={'input_type': 'password'}

    )
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
        if re.match(pattern, value):
            return value
        else:
            raise serializers.ValidationError("Invalid password")

    def validate_passward_confirmation(self, value):
        password = self.get_initial().get('password')
        if password != value:
            raise serializers.ValidationError("Password must be same")

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
