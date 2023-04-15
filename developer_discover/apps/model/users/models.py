from email.policy import default
from importlib.metadata import requires
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import UserManager
from django.db import models


class User(AbstractUser, PermissionsMixin):
    """유저 모델입니다.
    Notes:
        유저 아이디, 패스워드로 구성되고, 유저 식별 외 개인정보를 담지 않습니다.
    """

    username = models.CharField(
        "아이디",
        max_length=256,
        unique=True,
    )
    name = models.CharField(
        "이름",
        max_length=256,
        default="",
        blank=True,
    )
    introduction = models.TextField(
        "소개",
        max_length=2048,
        default="",
        null=True,
    )
    is_staff = models.BooleanField(
        "스태프 권한",
        default=False,
    )

    class Meta:
        db_table = "users"
        verbose_name = "user"
        verbose_name_plural = "users"
        swappable = "AUTH_USER_MODEL"

    def __str__(self):
        return f"[{self.id}] {self.name}"
