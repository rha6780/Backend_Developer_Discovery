from django.db import models


class Video(models):
    """유트브 강의
    Notes:
        유튜브 강의 정보를 저장하는 테이블입니다. 강의의 링크 부터 정보, 제목 등으로 식별가능합니다.
        기능 상 필요한 필드들이 있습니다.
    """

    title = models.CharField(
        "제목",
        max_length=512,
        default="",
        blank=True,
    )
    introduction = models.TextField(
        "소개",
        max_length=1024,
        default="",
        blank=True,
    )
    youtube_link = models.CharField(
        "유튜브 링크",
        max_length=2048,
        default="",
        blank=True,
    )

    class Meta:
        db_table = "videos"
        verbose_name = "video"
        verbose_name_plural = "videos"

    def __str__(self):
        return f"{self.title}"
