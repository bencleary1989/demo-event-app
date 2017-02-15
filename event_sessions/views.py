from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *


class SessionList(APIView):
    """
    List All Sessions
    """
    def get(self, request, format=None):
        sessions = EventSessions.objects.all()
        serializer = SessionSerializer(sessions, many=True)
        return Response(serializer.data)


class SessionAttendee(APIView):
    """
    Book sessions and view all specific attendees for session
    """
    def get(self, request, session, format=None):
        sessionattendees = SessionAttendees.objects.filter(session=session)
        serializer = SessionAttendeeSerializer(sessionattendees, many=True)
        return Response(serializer.data)

    # TODO add book function / Complete
    def post(self, request, format=None):
        serializer = SessionAttendeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

