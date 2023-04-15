from email.policy import default
from importlib.metadata import requires
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import UserManager
from django.db import models


class BasicUserManager(UserManager):
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError(_("Users must have an email address"))

        user = self.model(email=self.normalize_email(email), name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        pass  # ref: createsuperuser 에 password 필드 이름이 하드코딩 되어 있음.


class User(AbstractBaseUser, PermissionsMixin):
    """유저 모델입니다.
    Notes:
        유저 아이디, 패스워드로 구성되고, 유저 식별 외 개인정보를 담지 않습니다.
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
