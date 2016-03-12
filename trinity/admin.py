from django.contrib import admin
from.models import Question, TestStart, CorrectAnswers
# Register your models here.
admin.site.register(Question)
admin.site.register(TestStart)
admin.site.register(CorrectAnswers)