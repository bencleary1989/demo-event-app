from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import *


class VenueDetails(APIView):
    """
    Get the Venue Details
    """

    def get(self, request, format=None):
        eventvenue = EventVenueDetails.objects.first()
        serializer = VenueDetailsSerializer(eventvenue)
        return Response(serializer.data)