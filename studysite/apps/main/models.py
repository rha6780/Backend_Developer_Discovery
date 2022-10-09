from django.db import models


# Create your models here.
class Score(models.Model):
    name = models.CharField(max_length=200, default="user_name")
    score = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = "scores"


class Question(models.Model):
    category = models.CharField(max_length=50, default="")
    image = models.ImageField(upload_to=None, width_field=400, height_field=400)
    content = models.CharField(max_length=1_000, default="")
    answer_count = models.IntegerField(default=2)

    def __str__(self) -> str:
        return "[" + str(self.id) + "] : " + self.content

    class Meta:
        db_table = "questions"


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.CharField(max_length=1_000, default="")

    def __str__(self) -> str:
        return "[" + str(self.id) + "] : " + self.content

    class Meta:
        db_table = "answers"
