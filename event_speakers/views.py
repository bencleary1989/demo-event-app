from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *


class SpeakerList(APIView):
    """
    List All Speakers
    """

    def get(self, request, format=None):
        eventspeakers = EventSpeakers.objects.all()
        serializer = SpeakerSerializer(eventspeakers, many=True)
        return Response(serializer.data)


class SpeakerDetail(APIView):
    """
    Gets the chosen speakers profile
    """

    def get(self, request, uid, format=None):
        profile = SpeakerProfile.objects.get(profile_uid=uid)
        serializer = SpeakerProfileSerializer(profile)
        return Response(serializer.data)

