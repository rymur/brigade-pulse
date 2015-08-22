from django.db import models
from api.models import Brigade

from api.models.utils.trackable_model import TrackableModel


class MeetupEvent(TrackableModel):
    """
    Model for Meetup Events.
    """
    id = models.CharField(primary_key=True, max_length=255)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    venue_name = models.CharField(max_length=255, null=True, blank=True)
    group_name = models.CharField(max_length=255)
    event_url = models.URLField(max_length=1000)

    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True, blank=True)

    yes_rsvp_count = models.PositiveIntegerField(default=0)
    maybe_rsvp_count = models.PositiveIntegerField(default=0)
    waitlist_count = models.PositiveIntegerField(default=0)

    headcount = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField()

    brigade = models.ForeignKey(Brigade)

    class Meta(object):
        db_table = 'meetup_event'
        app_label = 'api'
