from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from ..core.models import TimeStampedModel


class Post(TimeStampedModel):
    title = (
        models.CharField(
            "제목",
            max_length=1024,
        ),
    )
    content = models.TextField(
        "내용",
        blank=False,
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="posts",
    )

    class Meta:
        db_table = "posts"
        verbose_name = "post"
        verbose_name_plural = "posts"

    def __str__(self):
        return f"[{self.id}] {self.title}"
