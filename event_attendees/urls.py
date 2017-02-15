from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^profile/$', AttendeeDetail.as_view())
]