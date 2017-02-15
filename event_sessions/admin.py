from django.contrib import admin
from .models import *


class EventSessionsAdmin(admin.ModelAdmin):
    list_display = ('session_uid', 'event_title', 'event_date')
    exclude = ['session_uid']


class SessionAttendeesAdmin(admin.ModelAdmin):
    list_display = ('attendee', 'session')

admin.site.register(EventSessions, EventSessionsAdmin)
admin.site.register(SessionAttendees, SessionAttendeesAdmin)

