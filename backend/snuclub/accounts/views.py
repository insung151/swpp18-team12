from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.mail import EmailMessage
from .tokens import account_activation_token
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text


from accounts.models import User
from accounts.serializers import LoginSerializer, SignUpSerializer, ChangePasswordSerializer



class LoginApiView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(username=serializer.validated_data['email'],
                            password=serializer.validated_data['password'])
        if user is None:
            return Response({
                'message': 'Email verification is incomplete or your account information is incorrect.'
            }, status=status.HTTP_401_UNAUTHORIZED)

        login(request, user)
        return Response(
            self.serializer_class(user).data,
            status=status.HTTP_200_OK
        )


class LogoutApiView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        logout(request)
        return Response()


class SignUpApiView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = SignUpSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        current_site = get_current_site(request)
        mail_subject = 'Activate your snuclub account.'
        message = render_to_string('acc_active_email.html', {
            'user': serializer.data['username'],
            'domain': current_site.domain,
            'uid': serializer.data['username'],
            'token': account_activation_token.make_token(serializer.data['username']),
        })
        to_email = serializer.data['email']
        email = EmailMessage(
            mail_subject, message, to=[to_email]
        )
        email.send()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ChangePasswordAPIView(UpdateAPIView):
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        return self.request.user

    def update(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        if not user.check_password(serializer.validated_data.get("old_password")):
            return Response({"old_password": ["Wrong password"]},
                            status=status.HTTP_403_FORBIDDEN)
        user.set_password(serializer.validated_data.get("new_password"))
        user.save()
        return Response({'message': "Success"}, status=status.HTTP_200_OK)

class ActivateUserAPIView(APIView):
    permission_classes = (AllowAny,)
    def get(self, request, userid, token):
        try:
            user = User.objects.get(username=userid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is not None and account_activation_token.check_token(userid, token):
            user.is_active = True
            user.save()
            login(request, user)
            # return redirect('home')
            return Response({'message':'Thank you for your email confirmation. Now you can login your account.'})
        else:
            return Response({'message':'Activation link is invalid! username = {}'.format(userid)})