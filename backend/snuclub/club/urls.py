from django.urls import path

from club.views import ClubUserRatingListView

urlpatterns = [
    path('<int:pk>/rating/', ClubUserRatingListView.as_view())
]
