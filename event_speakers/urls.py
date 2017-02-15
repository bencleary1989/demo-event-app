from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^speakers/$', SpeakerList.as_view()),
    url(r'^speaker/(?P<uid>.*)/details/$', SpeakerDetail.as_view())
]
