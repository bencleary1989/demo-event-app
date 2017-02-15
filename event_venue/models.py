from __future__ import unicode_literals
from uuid import uuid4
from django.db import models

def imageuploadeto(instance, filename):
    return 'uploads/venue/{0}'.format(filename)


class EventVenueDetails(models.Model):
    venue_uid = models.UUIDField(unique=True, default=uuid4)
    venue_name = models.CharField(max_length=255)
    venue_description = models.TextField()
    venue_postcode = models.CharField(max_length=10)
    venue_telephone = models.CharField(max_length=12)
    venue_email = models.CharField(max_length=255)
    venue_photo = models.ImageField(blank=True, upload_to=imageuploadeto)

    class Meta:
        managed = True
        db_table = 'demo_venue_details'
        verbose_name = "Venue Detail"
        verbose_name_plural = "Venue Details"
