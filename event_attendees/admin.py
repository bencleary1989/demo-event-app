from django.contrib import admin
from .models import *


class AttendeeDetailsAdmin(admin.ModelAdmin):
    list_display = ('attendee_name', 'attendee_email', 'attendee_company')

# Register your models here.
admin.site.register(AttendeeDetails, AttendeeDetailsAdmin)
