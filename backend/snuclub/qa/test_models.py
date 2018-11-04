from unittest import TestCase

from django.contrib.auth import get_user_model

from accounts.models import UserProfile
from qa.models import Question, Answer

User = get_user_model()


class QaTestCase(TestCase):

    def test_question(self):
        user = User.objects.create_user(
            email='wetwag@naveaw.com',
            username='wetw',
            password='awgaw112'
        )
        UserProfile.objects.create(user=user)
        Question.objects.create(
            author=user.userprofile,
            content=''
        )

    def test_answer(self):
        user = User.objects.create_user(
            email='wewag@aveaw.com',
            username='wetw1',
            password='wgaw112'
        )
        UserProfile.objects.create(user=user)
        question = Question.objects.create(
            author=user.userprofile,
            content=''
        )
        Answer.objects.create(
            question=question,
            content=''
        )
