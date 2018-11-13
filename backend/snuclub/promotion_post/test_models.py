from django.test import TestCase
from promotion_post.models import PromotionPost, PromotionPostComment
# Create your tests here.
from club.models import Club
from django.contrib.auth import get_user_model
from accounts.models import UserProfile

User = get_user_model()


class PromotionPostTestCase(TestCase):
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

    def test_Promotion_post(self):
        test_post = PromotionPost(
            author=self.userprofile,
            club=self.club,
            title="test",
            content="test content"
        )
        self.assertEqual(test_post.content, 'test content')
        self.assertEqual(test_post.club.name, 'testClub')
        self.assertEqual(test_post.title, 'test')


class PromotionPostCommentTestCase(TestCase):
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
        self.test_post = PromotionPost(
            author=self.userprofile,
            club=self.club,
            title="test",
            content="test content"
        )
        self.test_post.save()

    def test_Promotion_post_comments(self):
        test_comment = PromotionPostComment(
            author = self.userprofile,
            promotion_post = self.test_post,
            content = 'test comment'
        )
        test_comment.save()
        checker = PromotionPostComment.objects.get(id=1)
        self.assertEqual(checker.content, 'test comment')
        self.assertEqual(checker.promotion_post.title, 'test')
