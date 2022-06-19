from django.db import models


# Create your models here.
class Score(models):
    name = models.CharField(max_length=200, default="user_name")
    score = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = "scores"


class Question(models):
    category = models.CharField(max_length=50)
    content = models.CharField(max_length=1_000)
    Answer_count = models.IntegerField(default=2)

    class Meta:
        db_table = 'questions'

class Answer(models):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.CharField(max_length=1_000)

class Meta:
        db_table = 'answers'
        