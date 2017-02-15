from __future__ import unicode_literals
from uuid import uuid4
from event_sessions.models import EventSessions
from django.db import models


def imageuploadeto(instance, filename):
    return 'uploads/speakers/{0}'.format(filename)


class EventSpeakers(models.Model):
    speaker_uid = models.UUIDField(unique=True, default=uuid4)
    speaker_name = models.CharField(max_length=255, verbose_name="Speaker Name")
    speaker_session = models.ForeignKey(EventSessions, on_delete=None, to_field="id", verbose_name="Leading Session")
    speaker_image = models.ImageField(blank=True, upload_to=imageuploadeto, verbose_name="Speaker Image")
    speaker_confirmed = models.BooleanField(default=True, verbose_name="Confirmed")
    speaker_profile = models.ForeignKey('SpeakerProfile', on_delete=models.CASCADE, to_field="profile_uid")
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __unicode__(self):
        return self.speaker_name

    class Meta:
        managed = True
        db_table = "demo_event_speakers"
        verbose_name = "Event Speaker"
        verbose_name_plural = "Event Speakers"


class SpeakerProfile(models.Model):
    profile_uid = models.UUIDField(unique=True, default=uuid4)
    speaker_email = models.CharField(max_length=255, blank=True)
    speaker_location = models.CharField(max_length=255, blank=True)
    speaker_url = models.CharField(max_length=255, blank=True)
    speaker_profile = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __unicode__(self):
        return "{0}".format(self.profile_uid)

    class Meta:
        managed = True
        db_table = "demo_speaker_profiles"
        verbose_name = "Speaker Profile"
        verbose_name_plural = "Speaker Profiles"