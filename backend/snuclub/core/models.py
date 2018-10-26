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
    author = models.ForeignKey(
        'accounts.UserProfile',
        on_delete=models.SET_NULL,
        null=True
    )
    event_post = models.ForeignKey(
        'event_post.EventPost',
        on_delete=models.CASCADE
    )

    content = models.TextField(blank=False)

    class Meta:
        abstract = True
