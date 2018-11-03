from django.db import models

from club.models import Club
from accounts.models import UserProfile
from core.mixins import TimestampedMixin
from core.models import Article, Comment


class EventPost(Article):
    """
    이벤트 게시글에 대한 모델입니다.
    """
    author = models.ForeignKey(
        'accounts.UserProfile',
        on_delete=models.SET_NULL,
        null=True,
        related_name='event_posts'
    )
    club = models.ForeignKey(
        'club.Club',
        on_delete=models.CASCADE,
        related_name='event_posts'
    )
    event_start = models.DateTimeField(blank=True, null=True)
    event_end = models.DateTimeField(blank=True, null=True)


class EventPostComment(Comment):
    """
    이벤트 게시글에 달리는 댓글의 모델입니다.
    """
    author = models.ForeignKey(
        'accounts.UserProfile',
        on_delete=models.SET_NULL,
        null=True,
        related_name='event_post_comments'
    )
    event_post = models.ForeignKey(
        'event_post.EventPost',
        on_delete=models.CASCADE,
        related_name='event_post_comments'
    )
