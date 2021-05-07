from django.db import models
from .settings import Kakshayein
# Create your models here.

class Kaksha(models.Model):
    name = models.CharField(max_length=10, choices=Kakshayein.choices)

class Subject(models.Model):
    name = models.CharField(null=False, blank=False, max_length=10)
    short_desc = models.TextField()
    thumbnail = models.ImageField(upload_to='subjects/', null=True)
    kaksha = models.ForeignKey(Kaksha, on_delete=models.DO_NOTHING)

class Unit(models.Model):
    name = models.CharField(null=False, blank=False, max_length=50)
    short_desc = models.TextField()
    thumbnail = models.ImageField(upload_to='units/', null=True)
    subject = models.ForeignKey(Subject,
        null=False, blank=False, on_delete=models.DO_NOTHING)

class Chapter(models.Model):
    name = models.CharField(null=False, blank=False, max_length=50)
    short_desc = models.TextField()
    thumbnail = models.ImageField(upload_to='chapters/', null=True)
    unit = models.ForeignKey(Unit, on_delete=models.DO_NOTHING)
