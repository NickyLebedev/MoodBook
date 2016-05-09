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
    user = models.ForeignKey(User, related_name="fk_doctor", default="")
    subscriber = models.ForeignKey(User, related_name="fk_user", default="")

#raitings
#user - raiting for records
#doctor - doctor's raiting
class UserDetails(models.Model):
    user = models.ForeignKey(User)
    value = models.FloatField(default=0)
    count = models.IntegerField(default=0)
    mark = models.FloatField(default=0)

    def updateRaitings(self, val):
        self.value += val
        self.count += 1
        self.mark = self.value / self.count





