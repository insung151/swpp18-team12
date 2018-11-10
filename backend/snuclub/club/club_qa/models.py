from django.conf import settings
from django.db import models


class ClubQuestion(models.Model):
    """
    동아리에 질문한 글을 저장하는 모델입니다.
    """
    # 대댓글
    club_question = models.ForeignKey(
        'self',
        models.CASCADE,
        null=True,
        blank=True
    )
    author = models.ForeignKey(
        'accounts.UserProfile',
        models.SET_NULL,
        related_name='club_questions',
        null=True
    )
    club = models.ForeignKey(
        'club.Club',
        models.CASCADE,
        related_name='club_questions'
    )
    content = models.TextField()

    @property
    def is_staff(self):
        return self.author in self.club.staff or\
               self.author == self.club.admin
