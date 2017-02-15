from __future__ import unicode_literals
from uuid import uuid4
from django.db import models


def imageuploadeto(instance, filename):
    return 'uploads/profiles/{0}/{1}'.format(instance.id, filename)


class AttendeeDetails(models.Model):
    """
    A simplified user profile
    """
    attendee_uid = models.UUIDField(unique=True, default=uuid4)
    attendee_name = models.CharField(max_length=255, verbose_name="Name")
    attendee_email = models.CharField(max_length=255, verbose_name="Email")
    attendee_job_title = models.CharField(max_length=150, verbose_name="Job Title")
    attendee_company = models.CharField(max_length=255, verbose_name="Company")
    attendee_profile = models.TextField(verbose_name="Your Profile")
    attendee_image = models.ImageField(verbose_name="Profile Picture", upload_to=imageuploadeto)
    attendee_phone = models.CharField(max_length=12, null=True, blank=True, verbose_name="Phone Number")
    attendee_url = models.CharField(max_length=255, null=True, blank=True, verbose_name="Website URL")
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        managed = True
        db_table = 'demo_attendee_details'
        verbose_name = "Attendee"
        verbose_name_plural = "Attendees"


class AttendeeNotes(models.Model):
    """
        Stores user notes in the cloud
    """
    attendee = models.ForeignKey('AttendeeDetails', on_delete=None, to_field="attendee_uid", related_name="attendee_notes")
    notes = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        managed = True
        db_table = 'demo_attendee_notes'
        verbose_name = 'Attendee Note'
        verbose_name_plural = "Attendee Notes"
