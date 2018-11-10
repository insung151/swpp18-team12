from unittest import TestCase

from django.contrib.auth import get_user_model

from accounts.models import UserProfile
from club.models import Club, ClubRating, Tag, ClubDetail
from club.user_rating.models import UserRating

User = get_user_model()


class ClubTestCase(TestCase):

    def test_club(self):
        user = User.objects.create_user(
            email='tttt@test.com',
            password='qwer123',
            username='tttt'
        )
        UserProfile.objects.create(user=user)
        club = Club(
            admin=user.userprofile,
            activity_type=1,
            category=2,
            subcategory=3,
        )
        club.save()

    def test_club_rating(self):
        user = User.objects.create_user(
            email='ttt@test.com',
            password='qwer123',
            username='ttt'
        )
        UserProfile.objects.create(
            user=user
        )
        club = Club.objects.create(
            admin=user.userprofile,
            activity_type=1,
            category=2,
            subcategory=3,
        )
        club_rating = ClubRating(club=club)
        UserRating.objects.create(
            user=user.userprofile,
            club=club,
            overall=1,
            operation=1,
            facility=1,
            newcomer=1,
            compulsory=1,
            meetfreq=1,
            age=1,
            friendliness=1,
            alcohol=1,
            comments=''
        )
        club_rating = ClubRating.objects.first()
        self.assertEqual(club_rating.overall_sum, 1)

    def test_tag(self):
        Tag.objects.create(
            name='tag'
         )

    def test_club_detail(self):
        user = User.objects.create_user(
            email='tt1t@test.com',
            password='qwer123',
            username='ttt1'
        )
        UserProfile.objects.create(user=user)
        club = Club.objects.create(
            admin=user.userprofile,
            activity_type=1,
            category=2,
            subcategory=3,
        )
        ClubDetail.objects.create(
            club=club,
        )
