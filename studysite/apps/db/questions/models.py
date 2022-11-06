from django.db import models

CATEGORY_LIST = [
    ('basic', '기본')
]

class Question(models.Model):
    category = models.CharField(max_length=50, default="", choices=CATEGORY_LIST)
    image = models.ImageField(upload_to="image/%Y/%m/%d", null=True)
    content = models.CharField(max_length=1_000, default="")
    answer_count = models.IntegerField(default=2)

    def __str__(self) -> str:
        return "[" + str(self.id) + "] : " + self.content

    class Meta:
        db_table = "questions"
