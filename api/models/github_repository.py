from django.db import models

from api.models.utils.trackable_model import TrackableModel


class GitHubRepository(TrackableModel):
    """
    Base class for a GitHub Repository
    """

    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    language = models.CharField(max_length=255, null=True, blank=True)
    contributors = models.BooleanField()  # TODO
    owner = models.BooleanField()  # TODO
    homepage = models.URLField(max_length=1000, null=True, blank=True)

    stargazers_count = models.IntegerField()
    watchers_count = models.IntegerField()
    forks_count = models.IntegerField()
    open_issues = models.IntegerField

    created_at = models.DateTimeField()

