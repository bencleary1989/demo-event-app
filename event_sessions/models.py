from __future__ import unicode_literals
from uuid import uuid4
from django.db import models
from event_attendees.models import AttendeeDetails

class EventSessions(models.Model):
    session_uid = models.UUIDField(unique=True, default=uuid4)
    event_title = models.CharField(max_length=255)
    event_description = models.TextField(null=True, blank=True)
    event_date = models.DateTimeField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __unicode__(self):
        return self.event_title

    class Meta:
        managed = True
        db_table = 'demo_event_sessions'
        verbose_name = "Event Session"
        verbose_name_plural = "Event Sessions"


class SessionAttendees(models.Model):
    """
    Simple Table no Admin registration or Admin Model is needed
    """
    session_attendee_uid = models.UUIDField(unique=True, default=uuid4)
    attendee = models.ForeignKey(AttendeeDetails, on_delete=models.CASCADE, to_field="attendee_uid")
    session = models.ForeignKey(EventSessions, on_delete=models.CASCADE, to_field="session_uid")
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        managed = True
        db_table = "demo_session_attendees"
        verbose_name = "Session Attendee"
        verbose_name_plural = "Session Attendees"
