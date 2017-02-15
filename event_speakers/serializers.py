from rest_framework import serializers
from .models import *
from event_sessions.serializers import SessionSerializer


class SpeakerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpeakerProfile
        fields = ('profile_uid', 'speaker_email', 'speaker_location', 'speaker_url', 'speaker_profile')


class SpeakerSerializer(serializers.ModelSerializer):
    speaker_session = SessionSerializer()
    speaker_profile = SpeakerProfileSerializer()

    class Meta:
        model = EventSpeakers
        fields = ('speaker_uid', 'speaker_name', 'speaker_session', 'speaker_image', 'speaker_profile')
