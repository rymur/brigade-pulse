from django.db import models
from api.models import Brigade

from api.models.utils.trackable_model import TrackableModel


class MeetupGroup(TrackableModel):
    """
    Model for Meetup Groups.
    """
    id = models.CharField(primary_key=True, max_length=255)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    organizer_name = models.CharField(max_length=255)

    topics = models.TextField(null=True, blank=True)
    rating = models.FloatField(null=True, blank=True)
    members = models.PositiveIntegerField()

    brigade = models.ForeignKey(Brigade)

    class Meta(object):
        db_table = 'meetup_group'
        app_label = 'api'
