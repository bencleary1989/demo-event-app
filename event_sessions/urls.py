from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^sessions/$', SessionList.as_view()),
    url(r'^attendees/(?P<session>.*>)/$', SessionAttendee.as_view()),
    # POST URL
    url(r'^attendees/attend/$', SessionAttendee.as_view())
]