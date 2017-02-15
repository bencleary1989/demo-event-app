from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *


class AttendeeDetail(APIView):
    """
    View all attendees, edit own profile
    """

    def get(self, request, format=None):
        attendess = AttendeeDetails.objects.all()
        serializer = AttendeeSerializer(attendess, many=True)
        return Response(serializer.data)

        # TODO add profile update / Completed

    def post(self, request, format=None):
        serializer = AttendeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id, format=None):
        attendee = AttendeeDetails.objects.get(attendee_uid=id)
        serializer = AttendeeSerializer(attendee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#TODO attendee note views