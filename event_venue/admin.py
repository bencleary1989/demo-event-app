from django.contrib import admin
from .models import *


class EventVenueDetailsAdmin(admin.ModelAdmin):
    list_display = ('venue_uid', 'venue_name', 'venue_postcode')

admin.site.register(EventVenueDetails, EventVenueDetailsAdmin)
