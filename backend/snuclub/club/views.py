from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from club.user_rating.models import UserRating
from club.user_rating.serializers import UserRatingListSerializer


class ClubUserRatingListView(ListAPIView):
    queryset = UserRating.objects.all()
    serializer_class = UserRatingListSerializer
    permission_classes = (AllowAny, )

    def get_queryset(self):
        return super(ClubUserRatingListView, self).get_queryset()\
            .filter(club_id=self.kwargs['pk'])
