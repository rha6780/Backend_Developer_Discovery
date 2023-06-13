from email.policy import default
from importlib.metadata import requires
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import UserManager
from django.contrib.auth.password_validation import validate_password
from django.db import models

from ..core.models import SoftDeletedModel


class BasicUserManager(UserManager):
    def _create_user(self, email, name, password, **extra_fields):
        if not email:
            raise ValueError(("Users must have an email address"))
        validate_password(password)
        user = self.model(email=self.normalize_email(email), name=name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, name, password, **extra_fields):
        return self._create_user(email, name, password, **extra_fields)

    def create_superuser(self, email, name, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        if not email:
            raise ValueError(("Users must have an email address"))
        return self._create_user(email, name, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin, SoftDeletedModel):
    """유저 모델입니다.
    Notes:
        유저 이메일, 패스워드로 구성되고, 유저 식별 외 개인정보를 담지 않습니다.
    TODO List:
        * 삭제 시 is_delete 로 관리되고 이후 email, name 등을 특정 값으로 변경하는 것으로 처리 필요.
    """

    email = models.EmailField(
        "이메일",
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
    activate = models.BooleanField("활성화 여부", default=True)

    objects = BasicUserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "name",
        "password",
    ]

    class Meta:
        db_table = "users"
        verbose_name = "user"
        verbose_name_plural = "users"
        swappable = "AUTH_USER_MODEL"

    def __str__(self):
        return f"[{self.id}] {self.name}"
