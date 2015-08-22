from django.db import models
from api.models.utils.trackable_model import TrackableModel


class Brigade(TrackableModel):
    id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    started_on = models.DateField(null=True, blank=True)
    website = models.URLField(max_length=1000)
    type = models.CharField(max_length=255)

    events_url = models.URLField(max_length=1000)
    rss = models.URLField(max_length=1000)

    class Meta(object):
        db_table = 'brigade'
        app_label = 'api'
