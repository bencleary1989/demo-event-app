from django.contrib import admin
from .models import *


class EventSpeakersAdmin(admin.ModelAdmin):
    list_display = ('speaker_uid', 'speaker_name', 'speaker_session', 'speaker_confirmed')
    exclude = ['speaker_uid']


class SpeakerProfileAdmin(admin.ModelAdmin):
    list_display = ("profile_uid", "speaker_email", "created_at")


admin.site.register(EventSpeakers, EventSpeakersAdmin)
admin.site.register(SpeakerProfile, SpeakerProfileAdmin)