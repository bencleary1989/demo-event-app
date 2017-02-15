from rest_framework import serializers
from .models import *

class AttendeeSerializer(serializers.ModelSerializer):
    """
        Removed the UID as default value is set when creating
    """
    class Meta:
        model = AttendeeDetails
        fields = ('id', 'attendee_name', 'attendee_email', 'attendee_job_title', 'attendee_company', 'attendee_image')


class AttendeeNotesSerializer(serializers.ModelSerializer):

    class Meta:
        model = AttendeeNotes
        fields = ('attendee', 'notes', 'updated_at')