from django.contrib import admin
from .models import Record, EmotionList, Mood, DoctorUsers

admin.site.register(Record)
admin.site.register(EmotionList)
admin.site.register(Mood)
admin.site.register(DoctorUsers)