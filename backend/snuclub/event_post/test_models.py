from django.test import TestCase
from event_post.models import EventPost, EventPostComment
# Create your tests here.
from club.models import Club
from django.contrib.auth import get_user_model
from accounts.models import UserProfile

User = get_user_model()


class EventPostTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='test@test.com',
            password='qwer1234',
            username='test1234'
        )
        self.userprofile = UserProfile(user=self.user)
        self.club = Club(
            name='testClub',
            admin=self.user.userprofile,
            activity_type=1,
            category=1,
            subcategory=1
        )

    def test_event_post(self):
        test_post = EventPost(
            author=self.userprofile,
            club=self.club,
            title="test",
            content="test content"
        )
        self.assertEqual(test_post.content, 'test content')
        self.assertEqual(test_post.club.name, 'testClub')
        self.assertEqual(test_post.title, 'test')


class EventPostCommentTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='test@test.com',
            password='qwer1234',
            username='test1234'
        )
        self.user.save()
        self.userprofile = UserProfile(user=self.user)
        self.userprofile.save()
        self.club = Club(
            name='testClub',
            admin=self.user.userprofile,
            activity_type=1,
            category=1,
            subcategory=1
        )
        self.club.save()
        self.test_post = EventPost(
            author=self.userprofile,
            club=self.club,
            title="test",
            content="test content"
        )
        self.test_post.save()
    def test_event_post_comments(self):
        test_comment = EventPostComment(
            author = self.userprofile,
            event_post = self.test_post,
            content = 'test comment'
        )
        test_comment.save()
        checker = EventPostComment.objects.get(id=1)
        self.assertEqual(checker.content, 'test comment')
        self.assertEqual(checker.event_post.title, 'test')
