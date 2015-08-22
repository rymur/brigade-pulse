from django.db import models

from api.models.utils.trackable_model import TrackableModel


class MeetupEvent(TrackableModel):
    """
    Model for Meetup Events.
    """
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    organization_name = models.CharField(max_length=255)
    event_url = models.URLField(max_length=1000)

    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True, blank=True)

    created_at = models.DateTimeField()

    class Meta(object):
        db_table = 'meetup_event'
        app_label = 'api'
