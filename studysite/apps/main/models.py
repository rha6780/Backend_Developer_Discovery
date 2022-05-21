from django.db import models


# Create your models here.
class Score(models):
    name = models.CharField(max_length=200, default="user_name")
    score = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = "Score"
