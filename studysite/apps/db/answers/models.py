from unicodedata import category
from django.db import models
from ..questions.models import CATEGORY_LIST


class Answer(models.Model):
    question = models.ForeignKey("questions.Question", on_delete=models.CASCADE)
    category = models.CharField(max_length=50, default="", choices=CATEGORY_LIST)
    content = models.CharField(max_length=1_000, default="")

    def __str__(self) -> str:
        return "[" + str(self.id) + "] : " + self.content

    class Meta:
        db_table = "answers"
