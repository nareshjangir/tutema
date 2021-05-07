from django.db import models
from .settings import QuestionType

# Create your models here.
class Question(models.Model):
    type = models.CharField(max_length=30, choices=QuestionType.choices)
    text = models.TextField()

class Answer(models.Model):
    answer = models.CharField(max_length=150)
    questions = models.ManyToManyField(Question)
