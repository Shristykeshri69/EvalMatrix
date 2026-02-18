

# Register your models here.

from django.contrib import admin
from .models import Exam, Question, Option

admin.site.register(Exam)
admin.site.register(Question)
admin.site.register(Option)