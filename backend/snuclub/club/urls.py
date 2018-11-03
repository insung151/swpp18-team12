from django.urls import path
from club.views import ClubUserRatingListView
from club.views import CreateClubApiView, ClubProfileImageApiView, ClubDetailApiView, ClubShortApiView,ClubAdminChangeApiView


urlpatterns = [
    path('new/', CreateClubApiView.as_view(), name='make club'),
    path('<int:club_id>/club_detail/', ClubDetailApiView.as_view(), name='club detail'),
    path('<int:club_id>/club_short/', ClubShortApiView.as_view(), name='club short'),
    path('<int:club_id>/change_profile/', ClubProfileImageApiView.as_view(), name='change profile image'),
    path('<int:club_id>/change_admin/', ClubAdminChangeApiView.as_view(), name='change admin'),
    path('<int:pk>/rating/', ClubUserRatingListView.as_view())
]
