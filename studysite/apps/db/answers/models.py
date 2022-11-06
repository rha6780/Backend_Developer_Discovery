from django.db import models


class Answer(models.Model):
    question = models.ForeignKey("questions.Question", on_delete=models.CASCADE)
    content = models.CharField(max_length=1_000, default="")

    def __str__(self) -> str:
        return "[" + str(self.id) + "] : " + self.content

    class Meta:
        db_table = "answers"
