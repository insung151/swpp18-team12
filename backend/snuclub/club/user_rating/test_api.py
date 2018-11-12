from django.contrib.auth.models import AnonymousUser
from rest_framework.test import APITestCase, APIClient

from accounts.models import User, UserProfile
from club.models import Club, ClubRating
from club.user_rating.models import UserRating
from club.user_rating.serializers import UserRatingSerializer


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
            email='testemail@gmail.com',
            username='testuser',
            password='testpwd123',
        )
        self.user.is_active = True
        self.user.save()
        self.user_profile = UserProfile.objects.create(
            user=self.user
        )
        self.club = Club.objects.create(
            admin=self.user_profile,
            activity_type=2,
            category=3,
            subcategory=18
        )
        ClubRating.objects.create(club=self.club)
        UserRating.objects.bulk_create([
            user_rating_generator(self.user_profile, self.club),
            user_rating_generator(self.user_profile, self.club),
            user_rating_generator(self.user_profile, self.club),
            user_rating_generator(self.user_profile, self.club),
        ])
        self.user_ratings = UserRating.objects.all()

    def test_user_rating_list(self):
        resp = self.client.get('/api/rating/')
        serializer = UserRatingSerializer(
            self.user_ratings,
            many=True,
            context={'request': MockRequest(AnonymousUser)}
        )
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data['results'], serializer.data)

    def test_user_rating_create(self):
        user = User.objects.create_user(
            email='testemail2@gmail.com',
            username='testuser2',
            password='testpwd123',
        )
        user.is_active = True
        user.save()
        UserProfile.objects.create(
            user=user
        )
        self.client.force_login(user)
        data = {
            'club': self.club.pk, 'overall': 4, 'operation': 3, 'facility': 3, 'newcomer': 3, 'compulsory': 3,
            'meetfreq': 3, 'age': 3, 'friendliness': 3, 'alcohol': 3, 'comments': '...'
        }
        resp = self.client.post('/api/rating/', data=data)
        self.assertEqual(resp.status_code, 201)

        resp = self.client.post('/api/rating/', data=data)
        self.assertEqual(resp.status_code, 400, "중복 평가 금지")

        self.client.logout()
        resp = self.client.post('/api/rating/', data=data)
        self.assertEqual(resp.status_code, 403)

    def test_user_rating_retrieve(self):
        url = f'/api/rating/{self.user_ratings[0].pk}/'
        resp = self.client.get(url)
        serializer = UserRatingSerializer(
            UserRating.objects.get(pk=self.user_ratings[0].pk),
            context={'request': MockRequest(AnonymousUser)}
        )
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data, serializer.data)

    def test_user_rating_update(self):
        self.client.login(
            username='testemail@gmail.com',
            password='testpwd123'
        )
        data = {
            'club': self.club.pk, 'overall': 1, 'operation': 1, 'facility': 1, 'newcomer': 1,   'compulsory': 3,
            'meetfreq': 3, 'age': 1, 'friendliness': 3, 'alcohol': 3, 'comments': ''
        }
        url = f'/api/rating/{self.user_ratings[0].pk}/'
        resp = self.client.put(url, data=data)
        self.assertEqual(resp.status_code, 200)

        resp = self.client.patch(url, data={'overall': 3})
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(UserRating.objects.get(pk=self.user_ratings[0].pk).overall, 3)

        self.client.logout()
        resp = self.client.post(url, data=data)
        self.assertEqual(resp.status_code, 403)

    def test_user_rating_delete(self):
        self.client.login(
            username='testemail@gmail.com',
            password='testpwd123'
        )
        url = f'/api/rating/{self.user_ratings[0].pk}/'
        resp = self.client.delete(url)
        self.assertEqual(resp.status_code, 204)

        self.client.logout()
        resp = self.client.delete(url)
        self.assertEqual(resp.status_code, 403)
