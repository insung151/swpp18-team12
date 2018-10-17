from django.urls import path

from accounts.views import LoginApiView, LogoutApiView, SignUpApiView

urlpatterns = [
    path('login/', LoginApiView.as_view(), name='login'),
    path('logout/', LogoutApiView.as_view(), name='logout'),
    path('signup/', SignUpApiView.as_view(), name='signup'),
]
