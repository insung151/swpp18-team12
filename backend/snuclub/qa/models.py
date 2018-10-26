from django.db import models

from core.mixins import TimestampedMixin


class Question(TimestampedMixin, models.Model):
    """
    사이트에 관련된 정보를 묻는 질문 모델입니다
    """
    author = models.ForeignKey(
        'accounts.UserProfile',
        related_name='questions',
        null=True,
        on_delete=models.SET_NULL
    )

    content = models.TextField()


class Answer(TimestampedMixin, models.Model):
    """
    질문에 대한 답변 모델 입니다
    사이트 관리자가 답변합니다
    """

    question = models.ForeignKey(
        Question,
        related_name='answers',
        on_delete=models.CASCADE
    )
    content = models.TextField()
