from django.contrib.auth.models import AnonymousUser
from rest_framework.test import APITestCase, APIClient

from accounts.models import User, UserProfile
from club.models import Club, Tag, ClubDetail, ClubRating
from club.serializers import ClubSearchSerializer
from club.user_rating.models import UserRating
from club.user_rating.serializers import UserRatingListSerializer


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
        serializer = UserRatingListSerializer(
            self.club.user_ratings,
            many=True,
            context={
                'request': MockRequest(AnonymousUser)
            }
        )
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data["results"], serializer.data)

    def test_club_search(self):
        tag_apple = Tag.objects.create(name='apple')
        tag_orange = Tag.objects.create(name='orange')
        club_guitar = Club.objects.create(
            admin=self.user_profile,
            name='guitar',
            activity_type=2,
            category=3,
            subcategory=18
        )
        club_guitar.user_rating_count = 0
        ClubDetail.objects.create(club=club_guitar)
        ClubRating.objects.create(club=club_guitar)
        club_drum = Club.objects.create(
            admin=self.user_profile,
            name='drum',
            activity_type=2,
            category=5,
            subcategory=15
        )
        club_drum.user_rating_count = 0
        ClubDetail.objects.create(club=club_drum)
        ClubRating.objects.create(club=club_drum)
        club_piano = Club.objects.create(
            admin=self.user_profile,
            name='piano',
            activity_type=3,
            category=11,
            subcategory=17
        )
        club_piano.user_rating_count = 0
        ClubDetail.objects.create(club=club_piano)
        ClubRating.objects.create(club=club_piano)
        club_guitar.tags.add(tag_apple)
        club_piano.tags.add(tag_orange)

        resp = self.client.get('/api/club/search/?keyword=u')
        data = resp.data['results']
        self.assertEqual(resp.status_code, 200)
        self.assertIn(ClubSearchSerializer(club_guitar).data, data)
        self.assertIn(ClubSearchSerializer(club_drum).data, data)
        self.assertNotIn(ClubSearchSerializer(club_piano).data, data)

        resp = self.client.get('/api/club/search/?keyword=apple')
        data = resp.data['results']
        self.assertEqual(resp.status_code, 200)
        self.assertIn(ClubSearchSerializer(club_guitar).data, data)
        self.assertNotIn(ClubSearchSerializer(club_drum).data, data)
        self.assertNotIn(ClubSearchSerializer(club_piano).data, data)

        resp = self.client.get('/api/club/search/?type=3')
        data = resp.data['results']
        self.assertEqual(resp.status_code, 200)
        self.assertNotIn(ClubSearchSerializer(club_guitar).data, data)
        self.assertNotIn(ClubSearchSerializer(club_drum).data, data)
        self.assertIn(ClubSearchSerializer(club_piano).data, data)

        resp = self.client.get('/api/club/search/?cat=11&sub=17')
        data = resp.data['results']
        self.assertEqual(resp.status_code, 200)
        self.assertNotIn(ClubSearchSerializer(club_guitar).data, data)
        self.assertNotIn(ClubSearchSerializer(club_drum).data, data)
        self.assertIn(ClubSearchSerializer(club_piano).data, data)
