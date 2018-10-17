from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.models import User
from accounts.serializers import LoginSerializer


class LoginApiView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer
    queryset = User.object.all()

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid()
        user = authenticate(username=serializer.validated_data['email'],
                            password=serializer.validated_data['password'])
        if user is None:
            return Response({
                'message': '이메일 또는 비밀번호를 확인해 주세요.'
            }, status=status.HTTP_401_UNAUTHORIZED)

        if not user.is_active:
            return Response({
                'message': '이메일 인증을 완료해주세요.'
            }, status=status.HTTP_401_UNAUTHORIZED)

        login(request, user)
        return Response(
            self.serializer_class(user).data,
            status=status.HTTP_200_OK
        )


class LogoutApiView(APIView):
    def get(self, request, *args, **kwargs):
        logout(request)
        return Response()
