from rest_framework import serializers
from .models import *


class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventSessions
        fields = ('id', 'session_uid', 'event_title', 'event_description', 'event_date')


class SessionAttendeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SessionAttendees
        fields = ('attendee', 'session')