from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from softdelete.models import SoftDeleteObject
from ..core.models import TimeStampedModel


class Post(TimeStampedModel, SoftDeleteObject):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="posts",
    )
    title = models.CharField(
        "제목",
        max_length=1024,
        blank=False,
    )
    content = models.TextField(
        "내용",
        blank=False,
    )
    thumbnail = models.ImageField(
        "썸네일",
        null=True,
        blank=True,
    )
    like = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="likes")

    class Meta:
        db_table = "posts"
        verbose_name = "post"
        verbose_name_plural = "posts"

    def __str__(self):
        return f"[{self.id}] {self.title}"
