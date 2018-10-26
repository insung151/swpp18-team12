from django.db import models
from club.models import Club
from accounts.models import UserProfile
from core.mixins import TimestampedMixin
from core.models import Article, Comment


class PromotionPost(Article):
    """
    홍보 게시글에 대한 모델입니다.
    """
    author = models.ForeignKey(
        'accounts.UserProfile',
        on_delete=models.SET_NULL,
        null=True,
        related_name='promotion_posts'
    )
    club = models.ForeignKey(
        'club.Club',
        on_delete=models.CASCADE,
        related_name='promotion_posts'
    )
    join_start = models.DateTimeField(blank=True, null=True)
    join_end = models.DateTimeField(blank=True, null=True)



class PromotionPostComment(Comment):
    """
    홍보 게시글에 달리는 댓글의 모델입니다.
    """
    pass
