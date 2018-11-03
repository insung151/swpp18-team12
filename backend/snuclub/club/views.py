from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from accounts.models import UserProfile, User
from club.serializers import ClubSerializer, ClubDetailSerializer, ChangeProfileImageSerializer, ChangeAdminSerializer
from club.models import Club
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


# Create your views here.
class CreateClubApiView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ClubSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(admin=request.user.userprofile)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ClubDetailApiView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ClubDetailSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(club=Club.objects.get(id=self.kwargs['club_id']))
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ClubShortApiView(UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ClubSerializer
    model = Club

    def update(self, request, *args, **kwargs):
        club = Club.objects.get(id=self.kwargs['club_id'])
        serializer = self.serializer_class(club, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class ClubProfileImageApiView(UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    model = Club
    serializer_class = ChangeProfileImageSerializer

    def update(self, request, *args, **kwargs):
        club = Club.objects.get(id=self.kwargs['club_id'])
        new_image = self.serializer_class.validated_data.get('profile_image')
        club.profile_image = new_image
        club.save()
        return Response({'message':'Success'}, status=status.HTTP_200_OK)


class ClubAdminChangeApiView(UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangeAdminSerializer

    def update(self, request, *args, **kwargs):
        club = Club.objects.get(id=self.kwargs['club_id'])
        new_admin = self.serializer_class.validated_data.get('admin')
        if User.objects.filter(username=new_admin).exists():
           club.admin = new_admin
           club.save()
           return Response({'message': 'Success'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'User does not exist!'}, status=status.HTTP_404_NOT_FOUND)
