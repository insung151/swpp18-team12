from django.db import models

from accounts.models import UserProfile
from core.constants import ACTIVITY_TYPE, CATEGORIES, SUBCATEGORIES
from core.mixins import TimestampedMixin
from core.utils import RandomFileName


class Tag(models.Model):
    """
    동아리 검색에 사용되는 태그 모델입니다
    """
    name = models.CharField(
        max_length=10,
        unique=True,
        db_index=True
    )


class Club(TimestampedMixin, models.Model):
    """
    동아리 모델입니다
    """
    # 동아리 이름
    name = models.CharField(max_length=30)

    # 동아리 최고 관리자
    admin = models.ForeignKey(
        UserProfile,
        on_delete=models.SET_NULL,
        null=True
    )

    # 동아리 관련 게시글을 쓸 수 있는 스태프
    staff = models.ManyToManyField(
        UserProfile,
        related_name='staffs'
    )

    activity_type = models.IntegerField(
        choices=ACTIVITY_TYPE
    )

    profile_image = models.ImageField(
        upload_to=RandomFileName("club/profile"),
        blank=True,
        null=True
    )
    short_description = models.TextField(blank=True)

    category = models.IntegerField(choices=CATEGORIES)
    subcategory = models.IntegerField(choices=SUBCATEGORIES)
    tags = models.ManyToManyField(Tag, related_name='clubs')


class ClubDetail(TimestampedMixin, models.Model):
    """
    동아리 세부정보 모델입니다
    """
    club = models.OneToOneField(Club, on_delete=models.CASCADE)

    # 가입 마감일
    join_due_datetime = models.DateTimeField(blank=True)

    # 가입 링크
    join_link = models.URLField(blank=True)

    # 동아리 링크
    site_link = models.URLField(blank=True)

    # 동아리 상세 설명
    long_description = models.TextField(blank=True)

    # 동아리 히스토리
    history = models.TextField(blank=True)

    # 조회수
    hit = models.IntegerField()
