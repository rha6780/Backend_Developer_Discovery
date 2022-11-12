from django.db import models
from ..questions.models import CATEGORY_LIST

# Create your models here.
class Score(models.Model):
    category = models.CharField(max_length=50, default="", choices=CATEGORY_LIST)
    name = models.CharField(max_length=200, default="user_name")
    score = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = "scores"
