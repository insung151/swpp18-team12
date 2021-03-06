from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from django.contrib.auth import get_user_model

from accounts.models import UserProfile

from .tokens import account_activation_token, password_forgot_token

User = get_user_model()


class AccountsLoginTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_accounts(self):

        client = self.client

        # create User
        url = '/api/accounts/signup/'
        data = {
            "email": "test@testcase.com",
            "password": "qwer1234",
            "password_confirmation": "qwer1234",
            "username": "google",
            "year_of_admission": 2000,
            "department": "cs"
        }
        response = client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsNotNone(User.objects.get(email='test@testcase.com'))
        self.assertIsNotNone(UserProfile.objects.get(user__email='test@testcase.com'))

        # Email verification test
        token = account_activation_token.make_token("google")
        vurl = '/api/accounts/activate/google/{}/'.format(token)
        response2 = client.get(vurl)
        self.assertEqual(response2.status_code, status.HTTP_200_OK)
        user = User.objects.get(email='test@testcase.com')
        self.assertEqual(user.is_active, True)

    def test_login_and_logout_api(self):
        # create_user
        user = User.objects.create_user(
            email='test2@testcase.com',
            password='qwer1234',
            username='username'
        )
        user.is_active = True
        user.save()

        url = '/api/accounts/login/'
        data = {
            "email": "test2@testcase.com",
            "password": "qwer1234"
        }
        response = self.client.post(url, data=data)

        assert response.status_code == 200
        assert response.json()['username'] == 'username'

        url = '/api/accounts/logout/'
        response = self.client.get(url)
        assert response.status_code == 200

        # already logged out
        response = self.client.get(url)
        assert response.status_code == 403

    def test_change_password(self):

        old_password = 'qwer1234'
        new_password = '1234qwer'

        # create_user
        user = User.objects.create_user(
            email='test12@testcase.com',
            password=old_password,
            username='username'
        )
        user.is_active = True
        user.save()
        self.client.login(
            username='test12@testcase.com',
            password=old_password
        )

        url = '/api/accounts/change_password/'
        data = {
            "old_password": old_password,
            'new_password': new_password
        }
        response = self.client.put(url, data=data)
        assert response.status_code == 200

        is_correct = self.client.login(
            username='test12@testcase.com',
            password=new_password)
        self.assertEqual(is_correct, True)


class PasswordForgetTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        # create_user
        self.user = User.objects.create_user(
            email='test2@testcase.com',
            password='qwer1234',
            username='username'
        )
        self.user.is_active = True
        self.user.save()

    def test_forget_password(self):
        url = '/api/accounts/forgot_password/'
        email = {
            'email':'test2@testcase.com'
        }
        new_password = {
            'new_password':'asdf4321'
        }
        response = self.client.post(url, data=email)
        token = password_forgot_token.make_token(self.user.username)
        vurl = '/api/accounts/forgot_password/username/{}/'.format(token)
        response = self.client.put(vurl, new_password)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        is_correct = self.client.login(
            username='test2@testcase.com',
            password='asdf4321')
        self.assertEqual(is_correct, True)
        is_false = self.client.login(
            username='test2@testcase.com',
            password='qwer1234')
        self.assertEqual(is_false, False)