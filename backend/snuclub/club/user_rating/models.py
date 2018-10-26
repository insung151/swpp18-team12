from django.db import models

from club.models import Club
from accounts.models import UserProfile
from core.mixins import TimestampedMixin


class UserRating(TimestampedMixin, models.Model):
    """
    유저들이 작성한 레이팅의 모델입니다.
    """
    user = models.ForeignKey(
        UserProfile,
        on_delete=models.SET_NULL,
        null=True
    )
    club = models.ForeignKey(
        Club,
        on_delete=models.CASCADE
    )

    # 종합적 평가
    overall = models.IntegerField()

    # 동아리가 목적에 따라 얼마나 잘 굴러가는지에 관한 레이팅입니다.
    operation = models.IntegerField()

    # 동아리 시설
    facility = models.IntegerField()

    # 동아리가 신입부원이 적응하기에 얼마나 좋은지에 관한 레이팅입니다.
    newcomer = models.IntegerField()

    # 활동의 강제성
    compulsory = models.IntegerField()

    # 동아리 모임이 얼마나 자주 있는지
    meetfreq = models.IntegerField()

    # 전체적인 나이대 분포
    age = models.IntegerField()

    # 친밀도, 친목을 얼마나 하는지
    friendliness = models.IntegerField()

    # 술자리 빈도수
    alcohol = models.IntegerField()

    # 유저가 하고싶은 말을 적는 코멘트
    comments = models.TextField(blank=True)
