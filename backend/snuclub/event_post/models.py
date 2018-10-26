from django.db import models

from club.models import Club
from accounts.models import UserProfile
from core.mixins import TimestampedMixin
from core.models import Article


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


class EventPostComment(TimestampedMixin, models.Model):
    """
    이벤트 게시글에 달리는 댓글의 모델입니다.
    """
    pass
