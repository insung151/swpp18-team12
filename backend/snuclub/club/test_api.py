from rest_framework.test import APITestCase, APIClient

from accounts.models import User, UserProfile
from club.models import Club
from club.user_rating.models import UserRating
from club.user_rating.serializers import UserRatingListSerializer


def user_rating_generator(user_profile, club):
    def r():
        from random import randint
        return randint(1, 10)
    return UserRating(user=user_profile, club=club, overall=r(), operation=r(), facility=r(), newcomer=r(), compulsory=r(),
                      meetfreq=r(), age=r(), friendliness=r(), alcohol=r(), comments=f'test{r()}')


class ClubTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            email='testemail@email.com',
            username='testuser',
            password='testpwd',
        )
        self.user_profile = UserProfile.objects.create(
            user=self.user
        )
        self.club = Club.objects.create(
            admin=self.user_profile,
            activity_type=2,
            category=3,
            subcategory=18
        )
        self.user_ratings = UserRating.objects.bulk_create([
            user_rating_generator(self.user_profile, self.club),
            user_rating_generator(self.user_profile, self.club),
            user_rating_generator(self.user_profile, self.club),
            user_rating_generator(self.user_profile, self.club),
        ])

    def test_user_rating_list(self):
        resp = self.client.get(f'/api/club/{self.club.id}/rating/')
        serializer = UserRatingListSerializer(self.club.user_ratings, many=True)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data, serializer.data)
