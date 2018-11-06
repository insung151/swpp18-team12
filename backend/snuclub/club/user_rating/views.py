from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from club.user_rating.models import UserRating
from club.user_rating.serializers import UserRatingSerializer
from core.permissions import IsUserRatingOwnerOrReadOnly


class UserRatingViewSet(ModelViewSet):
    queryset = UserRating.objects.all()
    serializer_class = UserRatingSerializer

    permission_classes = [IsAuthenticatedOrReadOnly, IsUserRatingOwnerOrReadOnly]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        if UserRating.objects.filter(club_id=data['club'], user=data['user']).exists():
            return Response(
                {'message': "이미 평가하셨습니다."},
                status=status.HTTP_400_BAD_REQUEST
            )
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
