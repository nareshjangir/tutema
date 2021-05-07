from django.db import models
from cms.models import Chapter

# Create your models here.

class Section(models.Model):
    name = models.CharField(null=False, blank=False, max_length=100)
    short_desc = models.TextField()
    chapter = models.ForeignKey(Chapter, on_delete=models.DO_NOTHING)

class Definition(models.Model):
    name = models.CharField(null=False, blank=False, max_length=100)
    short_desc = models.TextField()
    thumbnail = models.ImageField(upload_to='definitions/', null=True)
    section = models.ForeignKey(Section, on_delete=models.DO_NOTHING)

class Concept(models.Model):
    name = models.CharField(null=False, blank=False, max_length=100)
    short_desc = models.TextField()
    thumbnail = models.ImageField(upload_to='concepts/', null=True)
    definitions = models.ManyToManyField(Definition)
