from unittest import TestCase

from django.contrib.auth import get_user_model

from accounts.models import UserProfile
from club.models import Club
from club.user_rating.models import UserRating

User = get_user_model()


class UserRatingTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='testasdf@test.com',
            password='qwer1234',
            username='testabcd'
        )
        self.userprofile = UserProfile(user=self.user)
        self.club = Club(
            name='testClubasdf',
            admin=self.user.userprofile,
            activity_type=1,
            category=1,
            subcategory=1
        )


    def test_user_rating(self):
        test_rating = UserRating(
            user=self.userprofile,
            club=self.club,
            overall=1,
            operation=2,
            facility=3,
            newcomer=4,
            compulsory=5,
            meetfreq=4,
            age=3,
            friendliness=2,
            alcohol=1,
            comments="Stupid club"
        )
        self.assertEqual(test_rating.user, self.userprofile)
        self.assertEqual(test_rating.alcohol, 1)
        self.assertEqual(test_rating.club, self.club)
