from django.db import models


class TimeStampedModel(models.Model):
    """
    Notes:
        Post, Comment, Reply 등 사용자가 작성한 데이터의 작성일, 수정일 등을 저장하는 모델
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class SoftDeleteManager(models.Manager):
    use_for_related_fields = True

    def get_queryset(self):
        return super().get_queryset().filter(is_deleted__isTrue=True)


class SoftDeletedModel(models.Model):
    """
    Notes:
        Soft-Delete 와 관련된 모델로 실제로 삭제하는 것이 아니라 is_delete를 통해서 구분합니다.
        * 현재 DateTimefield로 할지 고민 중입니다.
    """

    is_deleted = models.BooleanField(default=False)

    def soft_delete(self):
        self.is_deleted = True
        self.save()

    def restore(self):
        self.is_deleted = False
        self.save()

    class Meta:
        abstract = True
