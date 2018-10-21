from django.urls import path

from accounts.views import LoginApiView, LogoutApiView, SignUpApiView, ChangePasswordAPIView,ActivateUserAPIView

urlpatterns = [
    path('login/', LoginApiView.as_view(), name='login'),
    path('logout/', LogoutApiView.as_view(), name='logout'),
    path('signup/', SignUpApiView.as_view(), name='signup'),
    path('change_password/', ChangePasswordAPIView.as_view(), name='change_password'),
    path(r'activate/<userid>/<token>/',ActivateUserAPIView.as_view(), name='activate'),
]
