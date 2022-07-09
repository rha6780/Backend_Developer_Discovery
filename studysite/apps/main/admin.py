from django.contrib import admin

from .models import Answer
from .models import Question
from .models import Score

# Register your models here.
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Score)
