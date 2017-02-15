from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^venue/details/', VenueDetails.as_view(), name="Venue Details")
]