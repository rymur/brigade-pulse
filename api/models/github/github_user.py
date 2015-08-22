from django.db import models

from api.models.utils.trackable_model import TrackableModel


class GitHubUser(TrackableModel):

    name = models.CharField(max_length=255)
    avatar_url = models.CharField(max_length=255, null=True, blank=True)

    class Meta(object):
        db_table = 'github_user'
        app_label = 'api'
