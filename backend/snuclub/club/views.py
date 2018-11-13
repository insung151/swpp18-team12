from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from accounts.models import UserProfile, User
from club.serializers import ClubSerializer, ClubDetailSerializer, ChangeProfileImageSerializer, ChangeAdminSerializer
from club.models import Club
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from core.permissions import IsClubAdminOrReadOnly, IsClubDetailAdminOrReadOnly
from club.user_rating.models import UserRating
from club.user_rating.serializers import UserRatingListSerializer
from django.core.exceptions import ObjectDoesNotExist


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
    permission_classes = (IsAuthenticatedOrReadOnly, IsClubDetailAdminOrReadOnly)
    serializer_class = ClubDetailSerializer

    def get(self, request, *args, **kwargs):
        try:
            club_detail = Club.objects.get(id=self.kwargs['club_id']).clubdetail
            serializer = self.serializer_class(club_detail)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({"message":"Club does not exist"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, *args, **kwargs):
        try:
            club_detail = Club.objects.get(id=self.kwargs['club_id']).clubdetail
            serializer = self.serializer_class(club_detail, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({"message":"Club does not exist"}, status=status.HTTP_404_NOT_FOUND)


class ClubShortApiView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,IsClubAdminOrReadOnly)
    serializer_class = ClubSerializer
    model = Club

    def put(self, request, *args, **kwargs):
        try:
            club = Club.objects.get(id=self.kwargs['club_id'])
            serializer = self.serializer_class(club, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({"message":"Club does not exist"}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, *args, **kwargs):
        try:
            club = Club.objects.get(id=self.kwargs['club_id'])
            serializer = self.serializer_class(club)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({"message":"Club does not exist"}, status=status.HTTP_404_NOT_FOUND)


class ClubProfileImageApiView(APIView):
    permission_classes = (IsClubAdminOrReadOnly,)
    model = Club
    serializer_class = ChangeProfileImageSerializer

    def put(self, request, *args, **kwargs):
        try:
            club = Club.objects.get(id=self.kwargs['club_id'])
            if club.admin.user != request.user:
                return Response(status=status.HTTP_403_FORBIDDEN)
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid()
            new_image = serializer.validated_data['profile_image']
            club.profile_image = new_image
            club.save()
            return Response({'message': 'Success'}, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({"message": "Club does not exist"}, status=status.HTTP_404_NOT_FOUND)


class ClubAdminChangeApiView(APIView):
    permission_classes = (IsClubAdminOrReadOnly,)
    serializer_class = ChangeAdminSerializer
    model = Club

    def put(self, request, *args, **kwargs):
        try:
            club = Club.objects.get(id=self.kwargs['club_id'])
            if club.admin.user != request.user:
                return Response(status=status.HTTP_403_FORBIDDEN)
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid()
            new_admin = serializer.validated_data['admin']
            if User.objects.filter(username=new_admin).exists():
                club.admin = User.objects.get(username=new_admin).userprofile
                club.save()
                return Response({'message': f'Success. Changed admin to {club.admin.username}'}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'User does not exist!'}, status=status.HTTP_404_NOT_FOUND)
        except ObjectDoesNotExist:
            return Response({"message":"Club does not exist"}, status=status.HTTP_404_NOT_FOUND)