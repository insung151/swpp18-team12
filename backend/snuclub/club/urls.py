from django.urls import path

from club.views import ClubUserRatingListView
from club.views import ClubSearchAPIView

urlpatterns = [
    path('<int:pk>/rating/', ClubUserRatingListView.as_view()),
    path('search/', ClubSearchAPIView.as_view(), name='search')
]
