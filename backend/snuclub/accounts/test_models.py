import datetime
from unittest import TestCase

from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.contrib.auth import get_user_model

User = get_user_model()


class UserTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='test@test.com',
            password='qwer1234',
            username='test1234'
        )

    def test_create_profile(self):
        from accounts.models import UserProfile
        assert not hasattr(self.user, 'userprofile')

        valid_data = {'user': self.user, "year_of_admission": 2000 , "department": "cs"}
        invalid_data = [
            {'user': self.user, "year_of_admission": 1000, "department": "cs"},
            {"year_of_admission": 1000, "department": "cs"}

        ]

        profile = UserProfile(**valid_data)

        # year of admission must be in (1800 ~ 2500)
        for data in invalid_data:
            with self.assertRaises(ValidationError):
                UserProfile(**data).save()

        profile.save()

        assert hasattr(self.user, 'userprofile')
        # Delete current cp for other test
        profile.delete()
