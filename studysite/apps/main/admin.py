from django.contrib import admin

from .models import Answer
from .models import Question
from .models import Score

# Register your models here.
admin.register(Question)
admin.register(Answer)
admin.register(Score)
