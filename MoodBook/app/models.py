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
    angry = models.IntegerField()
    happy = models.IntegerField()
    suprise = models.IntegerField()
    sadness = models.IntegerField()
    mood = models.ForeignKey(Mood)

class DoctorUsers(models.Model):
    doctor_id = models.IntegerField()
    user_id = models.IntegerField()
