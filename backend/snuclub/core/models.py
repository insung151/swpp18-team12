from django.db import models

from core.mixins import TimestampedMixin


class Article(TimestampedMixin, models.Model):
    title = models.CharField(
        max_length=50,
        blank=False
    )

    content = models.TextField(blank=False)

    hits = models.IntegerField(default=0)

    class Meta:
        abstract = True


class Comment(TimestampedMixin, models.Model):

    content = models.TextField(blank=False)

    class Meta:
        abstract = True
