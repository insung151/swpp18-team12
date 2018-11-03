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
        related_name='staffs',
        blank=True
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
    tags = models.ManyToManyField(
        Tag,
        related_name='clubs',
        blank=True
    )


class ClubDetail(TimestampedMixin, models.Model):
    """
    동아리 세부정보 모델입니다
    """
    club = models.OneToOneField(Club, on_delete=models.CASCADE)

    # 가입 마감일
    join_due_datetime = models.DateTimeField(
        blank=True,
        null=True
    )

    # 가입 링크
    join_link = models.URLField(blank=True)

    # 동아리 링크
    site_link = models.URLField(blank=True)

    # 동아리 상세 설명
    long_description = models.TextField(blank=True)

    # 동아리 히스토리
    history = models.TextField(blank=True)

    # 조회수
    hits = models.IntegerField(default=0)


class ClubRating(models.Model):
    """
    동아리 전체 평점을 관리하는 모델입니다
    새로운 평가가 등록될 때마다 업데이트 됩니다(추후에 변경 가능)
    """
    club = models.OneToOneField(Club, models.CASCADE)

    # 종합적 평가
    overall_sum = models.IntegerField(default=0)

    # 동아리가 목적에 따라 얼마나 잘 굴러가는지에 관한 레이팅입니다.
    operation_sum = models.IntegerField(default=0)

    # 동아리 시설
    facility_sum = models.IntegerField(default=0)

    # 동아리가 신입부원이 적응하기에 얼마나 좋은지에 관한 레이팅입니다.
    newcomer_sum = models.IntegerField(default=0)

    # 활동의 강제성
    compulsory_sum = models.IntegerField(default=0)

    # 동아리 모임이 얼마나 자주 있는지
    meetfreq_sum = models.IntegerField(default=0)

    # 전체적인 나이대 분포
    age_sum = models.IntegerField(default=0)

    # 친밀도, 친목을 얼마나 하는지
    friendliness_sum = models.IntegerField(default=0)

    # 술자리 빈도수
    alcohol_sum = models.IntegerField(default=0)

    def add(self, **kwargs):
        for field in kwargs:
            value = getattr(self, field + '_sum')
            setattr(self, field + '_sum', value + kwargs[field])
        self.save()
