from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class User(AbstractUser, PermissionsMixin):
    """깃 허브 연동 유저 모델입니다.
    Notes:
        깃허브 연동을 통해 유저 정보를 저장하는 테이블입니다. 유저 아이디, 토큰 등 소셜 로그인을 통한 정보 및
        기능 상 필요한 필드들이 있습니다.
    """

    GITHUB = "github"

    email = models.EmailField(
        "이메일",
        unique=True,
        db_index=True,
    )
    name = models.CharField(
        "이름",
        max_length=256,
        default="",
        blank=True,
    )
    introduction = models.TextField(
        "소개",
        max_length=256,
        default="",
        blank=True,
    )
    github_link = models.CharField(
        "깃허브 링크",
        max_length=256,
        default="",
        blank=True,
    )
    social_providers = models.JSONField(
        "프로바이더",
        default=dict,
        blank=True,
    )
    agreeded_at = models.DateTimeField(
        "동의 시간",
        blank=True,
        null=True,
    )
    locations = models.CharField(
        "위치",
        max_length=256,
        default="",
        blank=True,
    )

    class Meta(AbstractUser.Meta):
        db_table = "users"
        verbose_name = "user"
        verbose_name_plural = "users"
        swappable = "AUTH_USER_MODEL"

    def __str__(self):
        return f"{self.id}, {self.email}"
