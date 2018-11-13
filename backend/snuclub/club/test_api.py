from django.contrib.auth.models import AnonymousUser
from rest_framework.test import APITestCase, APIClient

from accounts.models import User, UserProfile
from club.models import Club
from club.user_rating.models import UserRating
from club.user_rating.serializers import UserRatingListSerializer
from club.serializers import ClubSerializer, ClubDetailSerializer, ChangeProfileImageSerializer, ChangeAdminSerializer


class MockRequest:
    def __init__(self, user):
        self.user = user


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
            password='qwer1234',
        )
        self.user.is_active = True
        self.user_profile = UserProfile.objects.create(
            user=self.user
        )
        self.user.save()
        self.club = Club.objects.create(
            admin=self.user_profile,
            name="test",
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
        serializer = UserRatingListSerializer(
            self.club.user_ratings,
            many=True,
            context={
                'request': MockRequest(AnonymousUser)
            }
        )
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data["results"], serializer.data)

    def test_club_detail(self):
        #login
        login_data = {
            "email": "testemail@email.com",
            "password": "qwer1234"
        }
        resp = self.client.post('/api/accounts/login/', data=login_data)
        self.assertEqual(resp.status_code, 200)

        # create
        club_data = {
            "name": "testClub",
            "profile_image": None,
            "activity_type": 1,
            "short_description": "a",
            "category": 1,
            "subcategory": 2,
            "tags": [
                {
                    "name": "tag2"
                },
                {
                    "name": "tag3"
                }
            ]
        }
        resp = self.client.post(f'/api/club/new/', data=club_data, format='json')
        self.assertEqual(resp.status_code, 201)

        # get short
        resp = self.client.get(f'/api/club/2/club_short/')
        self.assertEqual(resp.data['activity_type'], 1)

        # update short
        update_club_data = {
            "name": "testClub",
            "profile_image": None,
            "activity_type": 1,
            "short_description": "Edited description",
            "category": 1,
            "subcategory": 2,
            "tags": [
                {
                    "name": "tag2"
                },
                {
                    "name": "tag3"
                }
            ]
        }
        resp = self.client.put(f'/api/club/2/club_short/', data=update_club_data, format='json')
        self.assertEqual(resp.status_code, 200)

        # update detail
        update_club_detail_data = {
            "join_due_datetime": None,
            "join_link": "https://www.qw.com",
            "site_link": "https://www.afdc.com",
            "long_description": "blahblahblah",
            "history": "2001"
        }
        resp = self.client.put(f'/api/club/2/club_detail/', data=update_club_detail_data, format='json')
        self.assertEqual(resp.status_code, 200)

        # get detail
        resp = self.client.get(f'/api/club/2/club_detail/')
        self.assertEqual(resp.data['history'], "2001")