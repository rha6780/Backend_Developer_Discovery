from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from softdelete.models import SoftDeleteObject
from ..core.models import TimeStampedModel


class Comment(TimeStampedModel, SoftDeleteObject):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="comments",
    )
    post = models.ForeignKey(
        "posts.Post",
        on_delete=models.CASCADE,
        null=True,
        related_name="comments",
    )
    content = models.TextField(
        "내용",
        blank=False,
    )

    class Meta:
        db_table = "comments"
        verbose_name = "comment"
        verbose_name_plural = "comments"

    def __str__(self):
        return f"{self.id}"
