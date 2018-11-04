from django.urls import path

from accounts.views import LoginApiView, LogoutApiView, SignUpApiView, ChangePasswordAPIView,ActivateUserAPIView, ForgotPasswordAPIView, ResetPasswordAPIView

urlpatterns = [
    path('login/', LoginApiView.as_view(), name='login'),
    path('logout/', LogoutApiView.as_view(), name='logout'),
    path('signup/', SignUpApiView.as_view(), name='signup'),
    path('change_password/', ChangePasswordAPIView.as_view(), name='change_password'),
    path(r'activate/<username>/<token>/', ActivateUserAPIView.as_view(), name='activate'),
    path(r'forgot_password/', ForgotPasswordAPIView.as_view(), name='forgot'),
    path(r'forgot_password/<username>/<token>/', ResetPasswordAPIView.as_view(), name='reset_password'),
]
