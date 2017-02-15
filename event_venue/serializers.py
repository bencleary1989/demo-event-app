from rest_framework import serializers
from .models import EventVenueDetails


class VenueDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventVenueDetails
        fields = ('venue_name', 'venue_description', 'venue_postcode', 'venue_telephone', 'venue_email', 'venue_photo')