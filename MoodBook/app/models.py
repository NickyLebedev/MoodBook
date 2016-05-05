"""
Definition of models.
"""

from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Mood(models.Model):
    name = models.CharField(max_length=60)

class Record(models.Model):
    name = models.CharField(max_length=60)
    date = models.DateTimeField(auto_created=True)
    mood = models.ForeignKey(Mood)
    user = models.ForeignKey(User)


class EmotionList(models.Model):
    angry = models.IntegerField(max_length=10)
    happy = models.IntegerField(max_length=10)
    suprise = models.IntegerField(max_length=10)
    sadness = models.IntegerField(max_length=10)
    mood = models.ForeignKey(Mood)
