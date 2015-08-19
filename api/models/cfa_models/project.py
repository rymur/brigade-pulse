from django.db import models
from api import Brigade
from api.models.github_repository import GitHubRepository
from api.models.utils.trackable_model import TrackableModel


class Project(TrackableModel):
    """
    Base model for projects.
    """
    brigade = models.ForeignKey(Brigade)

    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    link_url = models.URLField(max_length=1000, null=True, blank=True)
    code_url = models.URLField(max_length=1000, null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    tags = models.TextField(null=True, blank=True)
    organization_name = models.CharField(max_length=255)
    github_repository = models.ForeignKey(GitHubRepository, null=True, blank=True)

    last_updated = models.DateTimeField(null=True, blank=True)
